import os
import config


def initialize_environment() -> str:
    """Initialize environment variables needed for TM API communication."""
    tm_access_token = os.environ.get("TM_ACCESS_TOKEN")
    tm_core_api_url = os.environ.get("TM_CORE_API_URL")
    environment = os.environ.get("ENVIRONMENT")

    if not tm_access_token:
        raise ValueError("Missing required Access Token environment variable")
    if not tm_core_api_url:
        raise ValueError("Missing required Core API URL environment variable")
    if not environment:
        raise ValueError("Missing required Environment environment variable")

    config.tm_core_api_url = tm_core_api_url
    config.tm_access_token = tm_access_token

    return environment
