from common import config
import requests
import json
from typing import Any, List
import logging

logger = logging.getLogger(__name__)
session = requests.Session()


def setup_http_client():
    session.headers = build_request_headers()


def make_api_call(http_method, endpoint, query_params=None, payload=None):
    url = construct_full_url(endpoint)
    if "X-Auth-Token" not in session.headers:
        setup_http_client()

    try:
        r = session.request(http_method, url, params=query_params, data=payload)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print(r.content)
        raise
    response = json.loads(r.content)
    return response


def build_request_headers():
    headers = {"X-Auth-Token": config.tm_token, "Content-Type": "application/json"}
    return headers


def construct_full_url(endpoint):
    return config.core_api_url + endpoint


def fetch_all_pages(
    http_method, endpoint, query_params, page_size=50, all_pages=True, result_limit=0
) -> List[Any]:
    results = []
    page_token = ""

    if result_limit != 0:
        page_size = min(page_size, result_limit)

    while True:
        query_params.update({"page_size": page_size, "page_token": page_token})
        resp = make_api_call(http_method, endpoint, query_params)
        results.extend(list(resp.values())[0])
        page_token = resp["next_page_token"] if "next_page_token" in resp else ""
        if (
            not all_pages
            or page_token == ""
            or (result_limit != 0 and len(results) >= result_limit)
        ):
            logger.debug(
                f"Stopping paginated request as no further results needed or available:"
                f" all_pages is {all_pages}, page_token is {page_token}\n result limit is"
                f"{result_limit} and retrieved {len(results)} already"
            )
            break

    return results
