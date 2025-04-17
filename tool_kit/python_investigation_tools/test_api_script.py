import sys
import os
import logging
import argparse

from tool_kit.helpers.environment import initialize_environment
from tool_kit.helpers.core_api_helper import setup_session_headers
from tool_kit.common.get_requests import list_flags

# Set up logging
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format="%(asctime)s.%(msecs)03d - %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Set up argument parser
parser = argparse.ArgumentParser(description="Report on all accounts in the system.")
parser.add_argument(
    "--status_filter",
    help="Comma-separated list of account statuses to filter by. "
    "Defaults to ACCOUNT_STATUS_OPEN and ACCOUNT_STATUS_PENDING_CLOSURE.",
)
parser.add_argument(
    "--opening_timestamp_from",
    help="ISO timestamp. Report on all accounts opened from this time onwards.",
)
parser.add_argument(
    "--opening_timestamp_to", help="ISO timestamp. Report on all accounts opened up to this time."
)


def main() -> None:
    """Main function to run the account reporting tool."""
    args = parser.parse_args()

    # Initialize environment and session
    initialize_environment()
    setup_session_headers()

    logger.info("Starting flags report generation")
    logger.info("Parsed Arguments: %s", args)

    status_filter = args.status_filter.split(",") if args.status_filter else None
    opening_timestamp_from = args.opening_timestamp_from
    opening_timestamp_to = args.opening_timestamp_to

    flags = None
    try:
        flags = list_flags()
        logger.info("Retrieved %d flags", len(flags))
    except Exception as e:
        logger.error("Failed to retrieve flags: %s", str(e))
        sys.exit(1)

    logger.info("Flags: %s", flags)


if __name__ == "__main__":
    main()
