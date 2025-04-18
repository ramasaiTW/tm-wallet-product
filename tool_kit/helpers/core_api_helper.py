import logging
from typing import Any, Dict, List, Optional
import requests
import config

logger = logging.getLogger(__name__)
session = requests.Session()


def setup_session_headers() -> None:
    """Set up default headers for the session."""
    session.headers.update(_build_default_headers())


def _build_default_headers() -> Dict[str, str]:
    """Generate default headers with authentication token."""
    return {"X-Auth-Token": config.tm_access_token, "Content-Type": "application/json"}


def _construct_url(endpoint: str) -> str:
    """Construct the full API URL from the base and endpoint."""
    return f"{config.tm_core_api_url}{endpoint}"


def send_api_request(
    method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, data: Optional[Any] = None
) -> Dict[str, Any]:
    """Send an API request and return the JSON response."""
    if "X-Auth-Token" not in session.headers:
        setup_session_headers()

    url = _construct_url(endpoint)

    try:
        response = session.request(method, url, params=params, data=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - Response: {response.content}")
        raise
    except Exception as err:
        logger.error(f"Unexpected error occurred: {err}")
        raise

    return response.json()


def load_paginated_data(
    method: str,
    endpoint: str,
    initial_params: Dict[str, Any] = None,
    page_size: int = 50,
    fetch_all_pages: bool = True,
    max_results: int = 0,
) -> List[Any]:
    """Fetch paginated results from the API."""
    results: List[Any] = []
    next_page_token: str = ""
    params = initial_params.copy()

    if max_results > 0:
        page_size = min(page_size, max_results)

    while True:
        params.update({"page_size": page_size, "page_token": next_page_token})

        response_data = send_api_request(method, endpoint, params=params)

        items = list(response_data.values())[0]  # Assuming the first value holds the data
        results.extend(items)

        next_page_token = response_data.get("next_page_token", "")

        if (
            not fetch_all_pages
            or not next_page_token
            or (max_results and len(results) >= max_results)
        ):
            logger.debug(
                "Pagination complete: fetch_all_pages=%s, next_page_token='%s', "
                "max_results=%d, retrieved_results=%d",
                fetch_all_pages,
                next_page_token,
                max_results,
                len(results),
            )
            break

    return results
