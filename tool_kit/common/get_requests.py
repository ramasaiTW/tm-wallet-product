from typing import Any
from helpers.core_api_helper import load_paginated_data, send_api_request


def list_account_schedule_tags(all_pages=True, page_size=500) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of results to be listed. Required. Min value: 1. Max value: 500.
    """

    return load_paginated_data(
        "get", "/v1/account-schedule-tags", page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_account_schedule_tags(ids=None) -> Any:
    """
    :param ids: A list of the IDs of the AccountScheduleTags that are to be retrieved. The 6.0 release will reduce the
    maximum number of IDs to 50. Required. Min count: 1. Max count: 500.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/account-schedule-tags:batchGet", query_params)


def list_account_migrations(all_pages=True, statuses=None, page_size=1000) -> Any:
    """
    :param all_pages: To get the all pages
    :param statuses: The statuses of account migrations; these are used to filter on. Optional.
    :param page_size: The number of results to be listed. Required; must be non-zero.
    The 6.0 release will reduce the maximum page size to 100. Required. Min value: 1. Max value: 1000.
    """
    if statuses is None:
        statuses = []

    query_params = {
        "statuses": statuses,
    }
    return load_paginated_data(
        "get",
        "/v1/account-migrations",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_account_migrations(ids=None) -> Any:
    """
    :param ids: A list of the IDs of account migrations that are to be retrieved. Required; must be non-empty.
    The 6.0 release will enforce a maximum number of IDs of 50. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/account-migrations:batchGet", query_params)


def list_account_schedule_assocs(all_pages=True, account_id=None, page_size=500) -> Any:
    """
    :param all_pages: To get the all pages
    :param account_id: The account ID that Account Schedule associations are to be listed for. Required.
    :param page_size: The number of results to be listed. Required. Min value: 1. Max value: 500.
    """
    if account_id is None:
        account_id = ""

    query_params = {
        "account_id": account_id,
    }
    return load_paginated_data(
        "get",
        "/v1/account-schedule-assocs",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def get_account_schedule_assoc(id=None) -> Any:
    """
    :param id: The ID of the Account Schedule association that is to be retrieved. Required.
    """
    return send_api_request("get", f"/v1/account-schedule-assocs/{id}")


def list_account_update_batches(all_pages=True, account_migration_ids=None, page_size=20) -> Any:
    """
    :param all_pages: To get the all pages
    :param account_migration_ids: The IDs of the account migrations that account update batches are to be listed for.
    Required; must be non-empty.
    :param page_size: The number of results to be listed. Required; must be non-zero. Required.
    Min value: 1. Max value: 20.
    """
    if account_migration_ids is None:
        account_migration_ids = []

    query_params = {
        "account_migration_ids": account_migration_ids,
    }
    return load_paginated_data(
        "get",
        "/v1/account-update-batches",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_account_update_batches(ids=None) -> Any:
    """
    :param ids: A list of the IDs of account update batches that are to be retrieved. Required; must be non-empty.
    Required. Min count: 1. Max count: 20.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/account-update-batches:batchGet", query_params)


def list_account_updates(all_pages=True, account_id=None, statuses=None, page_size=1000) -> Any:
    """
    :param all_pages: To get the all pages
    :param account_id: The ID of the account that updates are to be listed for. Required.
    :param statuses: Statuses of account updates to filter on. Optional.
    :param page_size: The number of results to be listed. Required; must be non-zero. The 6.0 release will
    reduce the maximum page size to 100. Required. Min value: 1. Max value: 1000.
    """
    if account_id is None:
        account_id = ""
    if statuses is None:
        statuses = []

    query_params = {
        "account_id": account_id,
        "statuses": statuses,
    }
    return load_paginated_data(
        "get", "/v1/account-updates", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def get_account_update(id=None) -> Any:
    """
    :param id: The ID of the account update that is to be retrieved. Required.
    """
    return send_api_request("get", f"/v1/account-updates/{id}")


def batch_get_account_updates(ids=None) -> Any:
    """
    :param ids: A list of the IDs of account updates that are to be retrieved. Required; must be non-empty.
    The 6.0 release will enforce a maximum number of IDs of 50. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/account-updates:batchGet", query_params)


def list_accounts(
    all_pages=True,
    stakeholder_id=None,
    page_size=1000,
    account_statuses=None,
    product_version_ids=None,
    opening_timestamp_range_from=None,
    opening_timestamp_range_to=None,
    closing_timestamp_range_from=None,
    closing_timestamp_range_to=None,
) -> Any:
    if stakeholder_id is None:
        stakeholder_id = ""
    if account_statuses is None:
        account_statuses = []
    if product_version_ids is None:
        product_version_ids = []
    if opening_timestamp_range_from is None:
        opening_timestamp_range_from = ""
    if opening_timestamp_range_to is None:
        opening_timestamp_range_to = ""
    if closing_timestamp_range_from is None:
        closing_timestamp_range_from = ""
    if closing_timestamp_range_to is None:
        closing_timestamp_range_to = ""

    query_params = {
        "stakeholder_id": stakeholder_id,
        "account_statuses": account_statuses,
        "product_version_ids": product_version_ids,
        "opening_timestamp_range.from": opening_timestamp_range_from,
        "opening_timestamp_range.to": opening_timestamp_range_to,
        "closing_timestamp_range.from": closing_timestamp_range_from,
        "closing_timestamp_range.to": closing_timestamp_range_to,
    }
    return load_paginated_data(
        "get", "/v1/accounts", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def list_account_param_timeseries(account_id=None) -> Any:
    """
    :param account_id: The account ID a parameter timeseries is to be retrieved for.
    """
    return send_api_request("get", f"/v1/accounts/{account_id}:paramTimeseries")


def get_account(
    id=None, fields_to_include=None, instance_param_vals_effective_timestamp=None
) -> Any:
    """
    :param id: The ID of the account to be retrieved. Required.
    :param fields_to_include: A list of fields to display, which are omitted by default. When set to
    INCLUDE_FIELD_DERIVED_INSTANCE_PARAM_VALS, derived Instance-level parameters will be displayed in
    the`derived_instance_param_vals` field.
    :param instance_param_vals_effective_timestamp: The returned instance and derived parameter values will be
    calculated as of this timestamp. Should be formatted as an RFC3339 timestamp.
    """
    if fields_to_include is None:
        fields_to_include = []
    if instance_param_vals_effective_timestamp is None:
        instance_param_vals_effective_timestamp = ""

    query_params = {
        "fields_to_include": fields_to_include,
        "instance_param_vals_effective_timestamp": instance_param_vals_effective_timestamp,
    }
    return send_api_request("get", f"/v1/accounts/{id}", query_params)


def list_account_attribute_values(
    all_pages=True, page_size=100, account_ids=None, attribute_names=None, effective_timestamps=None
) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The page size of Account Attribute values to be returned. Maximum 100. Required.
    :param account_ids: Account IDs to filter values on. Required.
    :param attribute_names: Attribute Names to filter values on. Required.
    :param effective_timestamps: Effective timestamp values to filter on, each to be passed to the `attribute_hook`
     calculation as `effective_datetime`. Formatted as an RFC3339 timestamp. If unspecified, defaults to a single
     effective timestamp using the current system time.
    """
    if account_ids is None:
        account_ids = []
    if attribute_names is None:
        attribute_names = []
    if effective_timestamps is None:
        effective_timestamps = []

    query_params = {
        "account_ids": account_ids,
        "attribute_names": attribute_names,
        "effective_timestamps": effective_timestamps,
    }
    return load_paginated_data(
        "get",
        "/v1/account-attribute-values",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def list_service_accounts(all_pages=True, service_account_statuses=None, page_size=100) -> Any:
    """
    :param all_pages: To get the all pages
    :param service_account_statuses: A list of service account statuses that may be used as logical OR
    filters for results. Optional.
    :param page_size: The number of results to be listed. Required; must have an integer value in the range 1-100.
    Required. Min value: 1. Max value: 100.
    """
    if service_account_statuses is None:
        service_account_statuses = []

    query_params = {
        "service_account_statuses": service_account_statuses,
    }
    return load_paginated_data(
        "get", "/v1/service-accounts", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def get_service_account(id=None) -> Any:
    """
    :param id: The ID of the service account that is to be retrieved.
    """
    return send_api_request("get", f"/v1/service-accounts/{id}")


def batch_get_service_accounts(ids=None) -> Any:
    """
    :param ids: A list of the IDs of service accounts that are to be retrieved. Required; must be non-empty.
    Required. Min length: 1 characters.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/service-accounts:batchGet", query_params)


def validate_token() -> Any:
    return send_api_request("get", "/v1/token:validate")


def list_balances_live(
    all_pages=True, account_ids=None, account_addresses=None, page_size=10000
) -> Any:
    """
    :param all_pages: To get the all pages
    :param account_ids: The IDs of the accounts the balances belong to. Required.
    :param account_addresses: Filters results by account address. Optional.
    :param page_size: The number of results to be retrieved. Required. Required. Min value: 1. Max value: 10000.
    """
    if account_ids is None:
        account_ids = []
    if account_addresses is None:
        account_addresses = []

    query_params = {
        "account_ids": account_ids,
        "account_addresses": account_addresses,
    }
    return load_paginated_data(
        "get", "/v1/balances/live", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def list_balances_time_range(
    all_pages=True,
    account_ids=None,
    account_addresses=None,
    from_time=None,
    to_time=None,
    page_size=10000,
    snapshot_timestamp=None,
) -> Any:
    """
    :param all_pages: To get the all pages
    :param account_ids: The IDs of the accounts the balances belong to. Required.
    :param account_addresses: Filters results by account address.
    :param from_time: The earliest time in the time range of the returned balances in UTC. Optional. If included,
    will also return the latest balance event before the `from_time` for comparison. If omitted, the results will
    start from the first available balance event. Formatted as an RFC3339 timestamp.
    :param to_time: The latest time in the time range of the returned balances in UTC. Optional. If omitted, the
    results will end at the last available balance event. Formatted as an RFC3339 timestamp.
    :param page_size: The number of results to be retrieved. Required. Required. Min value: 1. Max value: 10000.
    :param snapshot_timestamp: If supplied, the balances time range will take into account only those postings
    inserted into Vault up to this time, and exclude balance changes from any postings inserted after this time.
    Optional.
    """
    if account_ids is None:
        account_ids = []
    if account_addresses is None:
        account_addresses = []
    if from_time is None:
        from_time = ""
    if to_time is None:
        to_time = ""
    if snapshot_timestamp is None:
        snapshot_timestamp = ""

    query_params = {
        "account_ids": account_ids,
        "account_addresses": account_addresses,
        "from_time": from_time,
        "to_time": to_time,
        "snapshot_timestamp": snapshot_timestamp,
    }
    return load_paginated_data(
        "get",
        "/v1/balances/timerange",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def list_calendar_events(
    all_pages=True,
    calendar_ids=None,
    calendar_event_names=None,
    page_size=10,
    active_calendar_event=None,
    calendar_timestamp_range_from=None,
    calendar_timestamp_range_to=None,
) -> Any:
    """
    :param all_pages: To get the all pages
    :param calendar_ids: Filters by Calendars IDs; if this is not set, all Calendars will be included.
    :param calendar_event_names: Filters by Calendar Event names; if filter criteria are not given,
    all Calendar Event names will be listed.
    :param page_size: The number of results to be listed. Must be non-zero. Required.
    :param active_calendar_event:
    :param calendar_timestamp_range_from: The Timestamp range that the Calendar Event is valid for. This is an auto
    generated field to make the swagger compatible with the third party codegen tool.
    :param calendar_timestamp_range_to: The Timestamp range that the Calendar Event is valid for. This is an auto
    generated field to make the swagger compatible with the third party codegen tool.
    """
    if calendar_ids is None:
        calendar_ids = []
    if calendar_event_names is None:
        calendar_event_names = []
    if active_calendar_event is None:
        active_calendar_event = ""
    if calendar_timestamp_range_from is None:
        calendar_timestamp_range_from = ""
    if calendar_timestamp_range_to is None:
        calendar_timestamp_range_to = ""

    query_params = {
        "calendar_ids": calendar_ids,
        "calendar_event_names": calendar_event_names,
        "active_calendar_event": active_calendar_event,
        "calendar_timestamp_range.from": calendar_timestamp_range_from,
        "calendar_timestamp_range.to": calendar_timestamp_range_to,
    }
    return load_paginated_data(
        "get", "/v1/calendar-event", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def get_calendar_event(id=None) -> Any:
    """
    :param id: Maps the ID to the requested CalendarEvent.
    """
    return send_api_request("get", f"/v1/calendar-event/{id}")


def batch_get_calendar_events(ids=None) -> Any:
    """
    :param ids: Maps the Calendar ID to the requested Calendars.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/calendar-event:batchGet", query_params)


def get_bookkeeping_date(id=None) -> Any:
    """
    :param id: The associated Calendar to retrieve the next Bookkeeping Date for
    """
    return send_api_request("get", f"/v1/calendar/bookkeeping-date/{id}")


def calculate_calendar_period(calendar_id=None, timestamp=None) -> Any:
    """
    :param calendar_id: The Calendar ID that will be used when calculating the number of period resolution units
    from the Calendar's start epoch.
    :param timestamp: The latest time that the number of period resolution units is calculated up to. Defaults to the
     current time in UTC. Must be formatted as an RFC3339 timestamp.
    """
    if timestamp is None:
        timestamp = ""

    query_params = {
        "timestamp": timestamp,
    }
    return send_api_request("get", f"/v1/calendar/{calendar_id}:calculatePeriod", query_params)


def get_calendar(id=None) -> Any:
    """
    :param id: Maps the ID to the requested Calendar.
    """
    return send_api_request("get", f"/v1/calendar/{id}")


def list_calendars(all_pages=True, page_size=10, order_by=None, name_pattern_match=None) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of results to be listed. Must be non-zero. Required.
    :param order_by: The ordering of the results. Optional.
    :param name_pattern_match:
    """
    if order_by is None:
        order_by = []
    if name_pattern_match is None:
        name_pattern_match = None

    query_params = {
        "order_by": order_by,
        "name_pattern_match": name_pattern_match,
    }
    return load_paginated_data(
        "get", "/v1/calendars", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def list_contract_executions(
    all_pages=True,
    page_size=50,
    contract_event_ids=None,
    account_ids=None,
    plan_ids=None,
    or_fields=None,
    execution_timestamp_range_from=None,
    execution_timestamp_range_to=None,
) -> Any:
    if contract_event_ids is None:
        contract_event_ids = []
    if account_ids is None:
        account_ids = []
    if plan_ids is None:
        plan_ids = []
    if or_fields is None:
        or_fields = []
    if execution_timestamp_range_from is None:
        execution_timestamp_range_from = ""
    if execution_timestamp_range_to is None:
        execution_timestamp_range_to = ""

    query_params = {
        "contract_event_ids": contract_event_ids,
        "account_ids": account_ids,
        "plan_ids": plan_ids,
        "or_fields": or_fields,
        "execution_timestamp_range.from": execution_timestamp_range_from,
        "execution_timestamp_range.to": execution_timestamp_range_to,
    }
    return load_paginated_data(
        "get",
        "/v1/contract-executions",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def list_contract_module_versions(all_pages=True, contract_module_id=None, page_size=20) -> Any:
    """
    :param all_pages: To get the all pages
    :param contract_module_id: The Contract Module ID to retrieve values for. Required.
    :param page_size: The number of Contract Module Versions to be retrieved. Required. Min value: 1. Max value: 20.
    """
    if contract_module_id is None:
        contract_module_id = ""

    query_params = {
        "contract_module_id": contract_module_id,
    }
    return load_paginated_data(
        "get",
        "/v1/contract-module-versions",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_contract_module_versions(ids=None, fields_to_include=None) -> Any:
    """
    :param ids: List of IDs of the Contract Module Versions to retrieve.
    :param fields_to_include: Additional fields to return; optional. Some Contract Module Version fields are
    omitted by default as they are bulky or costly; if those fields are specified here,
    they will be populated in the response.
    """
    if ids is None:
        ids = []
    if fields_to_include is None:
        fields_to_include = []

    query_params = {
        "ids": ids,
        "fields_to_include": fields_to_include,
    }
    return send_api_request("get", "/v1/contract-module-versions:batchGet", query_params)


def list_contract_modules(all_pages=True, page_size=50) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of Contract Modules to be retrieved. Required. Min value: 1. Max value: 50.
    """

    return load_paginated_data(
        "get", "/v1/contract-modules", page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_contract_modules(ids=None) -> Any:
    """
    :param ids: List of IDs of the Contract Modules to retrieve.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/contract-modules:batchGet", query_params)


def list_smart_contract_module_versions_links(
    all_pages=True, smart_contract_version_ids=None, contract_module_version_ids=None, page_size=50
) -> Any:
    """
    :param all_pages: To get the all pages
    :param smart_contract_version_ids: The Smart Contract Version IDs to retrieve values for.
    :param contract_module_version_ids: The Contract Module Version IDs to retrieve values for.
    :param page_size: The number of Contract Module Versions to be retrieved. Required. Min value: 1. Max value: 50.
    """
    if smart_contract_version_ids is None:
        smart_contract_version_ids = []
    if contract_module_version_ids is None:
        contract_module_version_ids = []

    query_params = {
        "smart_contract_version_ids": smart_contract_version_ids,
        "contract_module_version_ids": contract_module_version_ids,
    }
    return load_paginated_data(
        "get",
        "/v1/smart-contract-module-versions-links",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_smart_contract_module_versions_links(ids=None) -> Any:
    """
    :param ids: List of IDs of the Smart Contract Module Versions Links to retrieve.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request(
        "get", "/v1/smart-contract-module-versions-links:batchGet", query_params
    )


def list_customer_addresses(
    all_pages=True, customer_id=None, include_previous=None, page_size=1000
) -> Any:
    """
    :param all_pages: To get the all pages
    :param customer_id: The unique ID of the customer. Required.
    :param include_previous: Includes previous addresses for the customer. A previous address has an end_timestamp
    which is in the past. Optional; defaults to false.
    :param page_size: The number of addresses to be retrieved. Required. Min value: 1. Max value: 1000.
    """
    if customer_id is None:
        customer_id = ""
    if include_previous is None:
        include_previous = False

    query_params = {
        "customer_id": customer_id,
        "include_previous": include_previous,
    }
    return load_paginated_data(
        "get",
        "/v1/customer-addresses",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def list_customers(
    all_pages=True,
    statuses=None,
    email_identifiers=None,
    phone_identifiers=None,
    username_identifiers=None,
    page_size=200,
) -> Any:
    """
    :param all_pages: To get the all pages
    :param statuses: List of inclusive OR customer status filters. Optional.
    :param email_identifiers: List of inclusive OR email identifier filters. Must be URL encoded. Optional.
    :param phone_identifiers: List of inclusive OR phone number identifier filters. Must be URL encoded. Optional.
    :param username_identifiers: List of inclusive OR username identifier filters. Must be URL encoded. Optional.
    :param page_size: Number of customers to be listed. Required. Min value: 1. Max value: 200.
    """
    if statuses is None:
        statuses = []
    if email_identifiers is None:
        email_identifiers = []
    if phone_identifiers is None:
        phone_identifiers = []
    if username_identifiers is None:
        username_identifiers = []

    query_params = {
        "statuses": statuses,
        "email_identifiers": email_identifiers,
        "phone_identifiers": phone_identifiers,
        "username_identifiers": username_identifiers,
    }
    return load_paginated_data(
        "get", "/v1/customers", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def get_customer(customer_id=None) -> Any:
    """
    :param customer_id: The unique ID of the customer.
    """
    return send_api_request("get", f"/v1/customers/{customer_id}")


def batch_get_customers(ids=None) -> Any:
    """
    :param ids: A list of the IDs of customers that are to be retrieved. Required. Min length: 1 characters.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/customers:batchGet", query_params)


def get_derived_parameter_values(account_id=None, effective_timestamp=None) -> Any:
    """
    :param account_id: The Account ID for which derived parameters are calculated for.
    :param effective_timestamp: The returned derived parameter values will be calculated as of this timestamp.
    Defaults to the current time in UTC. Should be formatted as an RFC3339 timestamp.
    """
    if account_id is None:
        account_id = ""
    if effective_timestamp is None:
        effective_timestamp = ""

    query_params = {
        "account_id": account_id,
        "effective_timestamp": effective_timestamp,
    }
    return send_api_request("get", "/v1/derived-parameter-values", query_params)


def list_journal_events(all_pages=True, time_window=None, resource_type=None, page_size=100) -> Any:
    """
    :param all_pages: To get the all pages
    :param time_window:
    :param resource_type: The type of the Vault resource. Required.
    :param page_size: Number of results to be retrieved. Required. Required. Min value: 1. Max value: 100.
    """
    if time_window is None:
        time_window = None
    if resource_type is None:
        resource_type = ""

    query_params = {
        "time_window": time_window,
        "resource_type": resource_type,
    }
    return load_paginated_data(
        "get", "/v1/journal-events", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def get_journal_events_checksum(time_window=None, resource_type=None) -> Any:
    """
    :param time_window:
    :param resource_type: The type of the Vault resource. Required.
    """
    if time_window is None:
        time_window = None
    if resource_type is None:
        resource_type = ""

    query_params = {
        "time_window": time_window,
        "resource_type": resource_type,
    }
    return send_api_request("get", "/v1/journal-events:checksum", query_params)


def list_flag_definitions(
    all_pages=True,
    flag_visibility_level=None,
    flag_levels=None,
    include_inactive=None,
    page_size=500,
) -> Any:
    """
    :param all_pages: To get the all pages
    :param flag_visibility_level: The Flag visibility level that Flag Definitions are to be returned for. Set this to
    FLAG_VISIBILITY_OPERATOR to return Flag Definitions with Flag visibility=FLAG_VISIBILITY_OPERATOR. Set this to
    FLAG_VISIBILITY_CONTRACT to return all Flag Definitions. Optional.
    :param flag_levels: The Flag levels in the Flag Definition. If unspecified,
    this is equivalent to all Flag levels. Optional.
    :param include_inactive: Indicates whether inactive Flag Definitions are included. Optional.
    :param page_size: Number of results to be retrieved. Required; must be non-zero. The Vault Core 6.0 release will
    reduce the maximum page size to 100. Required. Min value: 1. Max value: 500.
    """
    if flag_visibility_level is None:
        flag_visibility_level = ""
    if flag_levels is None:
        flag_levels = []
    if include_inactive is None:
        include_inactive = False

    query_params = {
        "flag_visibility_level": flag_visibility_level,
        "flag_levels": flag_levels,
        "include_inactive": include_inactive,
    }
    return load_paginated_data(
        "get", "/v1/flag-definitions", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_flag_definitions(ids=None) -> Any:
    """
    :param ids: The Flag Definition IDs or names to be retrieved. The Vault Core 6.0 release will enforce a
    maximum number of IDs of 50.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/flag-definitions:batchGet", query_params)


def list_flags(
    all_pages=True,
    flag_definition_id=None,
    customer_ids=None,
    account_ids=None,
    payment_device_ids=None,
    flag_visibility_level=None,
    effective_timestamp=None,
    include_inactive=None,
    page_size=3000,
    effective_timestamp_range_from=None,
    effective_timestamp_range_to=None,
) -> Any:
    if flag_definition_id is None:
        flag_definition_id = ""
    if customer_ids is None:
        customer_ids = []
    if account_ids is None:
        account_ids = []
    if payment_device_ids is None:
        payment_device_ids = []
    if flag_visibility_level is None:
        flag_visibility_level = ""
    if effective_timestamp is None:
        effective_timestamp = ""
    if include_inactive is None:
        include_inactive = False
    if effective_timestamp_range_from is None:
        effective_timestamp_range_from = ""
    if effective_timestamp_range_to is None:
        effective_timestamp_range_to = ""

    query_params = {}
    return load_paginated_data(
        "get", "/v1/flags", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_flags(ids=None) -> Any:
    """
    :param ids: The Flag Definition IDs or names to be retrieved. The maximum number of IDs is 50.
    Required. Max count: 50.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/flags:batchGet", query_params)


def list_global_parameter_values(
    all_pages=True,
    global_parameter_id=None,
    page_size=100,
    effective_timestamp_range_from=None,
    effective_timestamp_range_to=None,
) -> Any:
    if global_parameter_id is None:
        global_parameter_id = ""
    if effective_timestamp_range_from is None:
        effective_timestamp_range_from = ""
    if effective_timestamp_range_to is None:
        effective_timestamp_range_to = ""

    query_params = {
        "global_parameter_id": global_parameter_id,
        "effective_timestamp_range.from": effective_timestamp_range_from,
        "effective_timestamp_range.to": effective_timestamp_range_to,
    }
    return load_paginated_data(
        "get",
        "/v1/global-parameter-values",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def list_global_parameters(all_pages=True, page_size=100) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of `GlobalParameter`s to be retrieved. Required. Min value: 1. Max value: 100.
    """

    return load_paginated_data(
        "get", "/v1/global-parameters", page_size=page_size, fetch_all_pages=all_pages
    )


def get_global_parameter(id=None) -> Any:
    """
    :param id: The ID of the `GlobalParameter` to be retrieved.
    """
    return send_api_request("get", f"/v1/global-parameters/{id}")


def batch_get_global_parameters(ids=None) -> Any:
    """
    :param ids: A list of IDs of `GlobalParameter`s to be retrieved.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/global-parameters:batchGet", query_params)


def list_internal_accounts(all_pages=True, view=None, page_size=1000) -> Any:
    """
    :param all_pages: To get the all pages
    :param view: The view of the data to return. Optional; default ACCOUNT_VIEW_BASIC.
    :param page_size: The number of results to be listed. Required; must be non-zero and no greater than 1000.
    The 6.0 release will reduce the maximum page size to 100. Required. Min value: 1. Max value: 1000.
    """
    if view is None:
        view = ""

    query_params = {
        "view": view,
    }
    return load_paginated_data(
        "get", "/v1/internal-accounts", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def get_internal_account(id=None, view=None) -> Any:
    """
    :param id: The ID of the internal account that is to be retrieved. Required.
    :param view: View of the data to return. Optional; default ACCOUNT_VIEW_BASIC.
    """
    if view is None:
        view = ""

    query_params = {
        "view": view,
    }
    return send_api_request("get", f"/v1/internal-accounts/{id}", query_params)


def batch_get_internal_accounts(ids=None, view=None) -> Any:
    """
    :param ids: A list of the IDs of internal accounts to be retrieved. Required; must be non-empty.
    The 6.0 release will enforce a maximum number of IDs of 50. Required. Min count: 1.
    :param view: View of the data to return. Optional; default ACCOUNT_VIEW_BASIC.
    """
    if ids is None:
        ids = []
    if view is None:
        view = ""

    query_params = {
        "ids": ids,
        "view": view,
    }
    return send_api_request("get", "/v1/internal-accounts:batchGet", query_params)


def list_ledger_balances(
    all_pages=True, account_ids=None, ledger_timestamp=None, page_size=10000
) -> Any:
    """
    :param all_pages: To get the all pages
    :param account_ids: The IDs of the accounts that Ledger Balances are to be listed for. Required.
    :param ledger_timestamp: The Postings Ledger timestamp at which to retrieve Ledger Balances.
    Must be formatted as an RFC3339 timestamp. Required.
    :param page_size: The number of results to be retrieved. Validated in the ledger balance service.
    Required. Min value: 1. Max value: 10000.
    """
    if account_ids is None:
        account_ids = []
    if ledger_timestamp is None:
        ledger_timestamp = ""

    query_params = {
        "account_ids": account_ids,
        "ledger_timestamp": ledger_timestamp,
    }
    return load_paginated_data(
        "get", "/v1/ledger-balances", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def get_ledger_balance(id=None) -> Any:
    """
    :param id: The ID of the Ledger Balance to be retrieved. Required.
    """
    return send_api_request("get", f"/v1/ledger-balances/{id}")


def list_parameter_value_hierarchy_nodes(
    all_pages=True, page_size=100, order_by=None, parent_ids=None, names=None
) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of Parameter Value Hierarchy Nodes to be returned. Maximum 100. Required.
    :param order_by: The order in which Parameter Value Hierarchy Nodes will be returned. When ordering results with
    the same value, Parameter Value Hierarchy Nodes will be sorted by ascending `parent_id` and then by ascending `id`.
    :param parent_ids: A set of Parameter Value Hierarchy Node IDs. Matches all Parameter Value Hierarchy Nodes with
    a `parent_id` in the set. Must not contain empty IDs.
    :param names: A set of names. Matches all Parameter Value Hierarchy Nodes with a `name` in the provided names.
     Must not contain empty strings.
    """
    if order_by is None:
        order_by = ""
    if parent_ids is None:
        parent_ids = []
    if names is None:
        names = []

    query_params = {
        "order_by": order_by,
        "parent_ids": parent_ids,
        "names": names,
    }
    return load_paginated_data(
        "get",
        "/v1/parameter-value-hierarchy-nodes",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_parameter_value_hierarchy_nodes(ids=None) -> Any:
    """
    :param ids: A list of Parameter Value Hierarchy Node IDs to retrieve. Maximum 100. Required.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/parameter-value-hierarchy-nodes:batchGet", query_params)


def list_parameter_values(
    all_pages=True,
    page_size=100,
    parameter_ids=None,
    global_param=None,
    account_config_group_ids=None,
    account_ids=None,
    is_cancelled=None,
    parameter_value_hierarchy_node_ids=None,
    effective_timestamp_range_from=None,
    effective_timestamp_range_to=None,
) -> Any:
    if parameter_ids is None:
        parameter_ids = []
    if global_param is None:
        global_param = False
    if account_config_group_ids is None:
        account_config_group_ids = []
    if account_ids is None:
        account_ids = []
    if is_cancelled is None:
        is_cancelled = ""
    if parameter_value_hierarchy_node_ids is None:
        parameter_value_hierarchy_node_ids = []
    if effective_timestamp_range_from is None:
        effective_timestamp_range_from = ""
    if effective_timestamp_range_to is None:
        effective_timestamp_range_to = ""

    query_params = {
        "parameter_ids": parameter_ids,
        "global": global_param,
        "account_config_group_ids": account_config_group_ids,
        "account_ids": account_ids,
        "is_cancelled": is_cancelled,
        "parameter_value_hierarchy_node_ids": parameter_value_hierarchy_node_ids,
        "effective_timestamp_range.from": effective_timestamp_range_from,
        "effective_timestamp_range.to": effective_timestamp_range_to,
    }
    return load_paginated_data(
        "get", "/v1/parameter-values", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_parameter_values(ids=None) -> Any:
    """
    :param ids: IDs of Parameter Values to retrieve. Maximum 100. Required.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/parameter-values:batchGet", query_params)


def list_parameters(all_pages=True, page_size=1000) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of Parameters to be returned. Maximum 1000. Required.
    """

    return load_paginated_data(
        "get", "/v1/parameters", page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_parameters(ids=None) -> Any:
    """
    :param ids: IDs of Parameters to retrieve. Maximum 100. Required.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/parameters:batchGet", query_params)


def list_payment_device_links(
    tokens=None,
    payment_device_ids=None,
    account_ids=None,
    effective_timestamp=None,
    include_inactive=None,
) -> Any:
    """
    :param tokens: List of payment device link tokens.
    :param payment_device_ids: List of payment device IDs.
    :param account_ids: List of account IDs.
    :param effective_timestamp: Maximum start timestamp of listed links. Optional. Defaults to current time.
    Must be formatted as an RFC3339 timestamp.
    :param include_inactive: Indicates whether to include inactive payment device links in the response.
    """
    if tokens is None:
        tokens = []
    if payment_device_ids is None:
        payment_device_ids = []
    if account_ids is None:
        account_ids = []
    if effective_timestamp is None:
        effective_timestamp = ""
    if include_inactive is None:
        include_inactive = False

    query_params = {
        "tokens": tokens,
        "payment_device_ids": payment_device_ids,
        "account_ids": account_ids,
        "effective_timestamp": effective_timestamp,
        "include_inactive": include_inactive,
    }
    return send_api_request("get", "/v1/payment-device-links", query_params)


def batch_get_payment_device_links(ids=None) -> Any:
    """
    :param ids: List of IDs of payment device links to fetch. Required; must be non-empty.
    The 6.0 release will enforce a maximum number of IDs of 50.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/payment-device-links:batchGet", query_params)


def batch_get_payment_devices(ids=None) -> Any:
    """
    :param ids: List of IDs of payment devices to fetch. Required; must be non-empty.
    The 6.0 release will enforce a maximum number of IDs of 50.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/payment-devices:batchGet", query_params)


def list_account_plan_assocs(
    all_pages=True,
    account_ids=None,
    plan_ids=None,
    page_size=100,
    start_timestamp_range_from=None,
    start_timestamp_range_to=None,
    end_timestamp_range_from=None,
    end_timestamp_range_to=None,
) -> Any:
    if account_ids is None:
        account_ids = []
    if plan_ids is None:
        plan_ids = []
    if start_timestamp_range_from is None:
        start_timestamp_range_from = ""
    if start_timestamp_range_to is None:
        start_timestamp_range_to = ""
    if end_timestamp_range_from is None:
        end_timestamp_range_from = ""
    if end_timestamp_range_to is None:
        end_timestamp_range_to = ""

    query_params = {
        "account_ids": account_ids,
        "plan_ids": plan_ids,
        "start_timestamp_range.from": start_timestamp_range_from,
        "start_timestamp_range.to": start_timestamp_range_to,
        "end_timestamp_range.from": end_timestamp_range_from,
        "end_timestamp_range.to": end_timestamp_range_to,
    }
    return load_paginated_data(
        "get",
        "/v1/account-plan-assocs",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_account_plan_assocs(ids=None) -> Any:
    """
    :param ids: A list of the IDs of the account Plan Associations that are to be retrieved.
    Required; must be non-empty. The 6.0 release will enforce a maximum number of IDs of 50. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/account-plan-assocs:batchGet", query_params)


def list_plan_migrations(all_pages=True, statuses=None, page_size=100) -> Any:
    """
    :param all_pages: To get the all pages
    :param statuses: Statuses of Plan Migrations to filter on. Optional.
    :param page_size: Number of results to be retrieved. Must be non-zero. Required. Min value: 1. Max value: 100.
    """
    if statuses is None:
        statuses = []

    query_params = {
        "statuses": statuses,
    }
    return load_paginated_data(
        "get", "/v1/plan-migrations", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_plan_migrations(ids=None) -> Any:
    """
    :param ids: IDs of the Plan Migrations to get. Mandatory.
    The 6.0 release will enforce a maximum number of IDs of 50. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/plan-migrations:batchGet", query_params)


def list_plan_schedules(
    all_pages=True, plan_id=None, page_size=20, include_disassociated=None
) -> Any:
    """
    :param all_pages: To get the all pages
    :param plan_id: The Plan ID that Plan Schedules are to be listed for. Required; must be non-empty.
    :param page_size: The number of results to be retrieved. Required. Required. Min value: 1. Max value: 20.
    :param include_disassociated: A boolean controlling the Plan Schedules that are returned. When set to `false`,
    only associated Plan Schedules, that is, Plan Schedules with `is_associated=true`, are returned.
    When set to `true`, associated and disassociated Plan Schedules are returned. An optional field. False by default.
    """
    if plan_id is None:
        plan_id = ""
    if include_disassociated is None:
        include_disassociated = False

    query_params = {
        "plan_id": plan_id,
        "include_disassociated": include_disassociated,
    }
    return load_paginated_data(
        "get", "/v1/plan-schedules", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def list_plan_updates(
    all_pages=True, plan_ids=None, job_ids=None, statuses=None, page_size=100
) -> Any:
    """
    :param all_pages: To get the all pages
    :param plan_ids: The IDs of Plans that Plan Updates are to be listed for. At least one of plan_ids and job_ids
    is required; must be non-empty.
    :param job_ids: IDs of the jobs that Plan Updates are to be listed for.
    At least one of plan_ids and job_ids is required.
    :param statuses: The statuses of Plan Updates to filter on. Optional.
    :param page_size: The number of results to be retrieved. Required. Required. Min value: 1. Max value: 100.
    """
    if plan_ids is None:
        plan_ids = []
    if job_ids is None:
        job_ids = []
    if statuses is None:
        statuses = []

    query_params = {
        "plan_ids": plan_ids,
        "job_ids": job_ids,
        "statuses": statuses,
    }
    return load_paginated_data(
        "get", "/v1/plan-updates", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_plan_updates(ids=None) -> Any:
    """
    :param ids: A list of the IDs of the Plan Updates that are to be retrieved. Required; must be non-empty.
    The 6.0 release will enforce a maximum number of IDs of 50. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/plan-updates:batchGet", query_params)


def batch_get_plans(ids=None) -> Any:
    """
    :param ids: A list of the IDs of the Plans that are to be retrieved. Required; must be non-empty. The 6.0 release
     will enforce a maximum number of IDs of 50. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/plans:batchGet", query_params)


def list_policies(
    all_pages=True, policy_schema_ids=None, fields_to_include=None, page_size=100
) -> Any:
    """
    :param all_pages: To get the all pages
    :param policy_schema_ids: The policy schema ID or IDs to filter results by. Optional.
    :param fields_to_include: Fields to include in the response that are omitted by default. Optional.
    :param page_size: The number of results to be listed. Required; must be non-zero. Maximum value of 100.
    Required. Min value: 1. Max value: 100.
    """
    if policy_schema_ids is None:
        policy_schema_ids = []
    if fields_to_include is None:
        fields_to_include = []

    query_params = {
        "policy_schema_ids": policy_schema_ids,
        "fields_to_include": fields_to_include,
    }
    return load_paginated_data(
        "get", "/v1/policies", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def get_policy(id=None) -> Any:
    """
    :param id: The ID of the Policy that is to be retrieved. Required.
    """
    return send_api_request("get", f"/v1/policies/{id}")


def batch_get_policies(ids=None, fields_to_include=None) -> Any:
    """
    :param ids: The IDs of the Policies to be retrieved. Required.
    :param fields_to_include: Fields to include in the response that are omitted by default. Optional.
    """
    if ids is None:
        ids = []
    if fields_to_include is None:
        fields_to_include = []

    query_params = {
        "ids": ids,
        "fields_to_include": fields_to_include,
    }
    return send_api_request("get", "/v1/policies:batchGet", query_params)


def list_post_posting_failures(
    all_pages=True,
    account_ids=None,
    posting_instruction_batch_ids=None,
    page_size=50,
    post_posting_failure_statuses=None,
) -> Any:
    """
    :param all_pages: To get the all pages
    :param account_ids: Filters Post-Posting Failures by the account IDs of their associated failures. Optional.
    :param posting_instruction_batch_ids: Filters Post-Posting Failures by the posting instruction batch IDs of their
    associated failures. Optional.
    :param page_size: The number of Post-Posting Failures to be retrieved. Required. Min value: 1. Max value: 50.
    :param post_posting_failure_statuses: Filters Post Posting Failures by the provided failure status. Optional.
    """
    if account_ids is None:
        account_ids = []
    if posting_instruction_batch_ids is None:
        posting_instruction_batch_ids = []
    if post_posting_failure_statuses is None:
        post_posting_failure_statuses = []

    query_params = {
        "account_ids": account_ids,
        "posting_instruction_batch_ids": posting_instruction_batch_ids,
        "post_posting_failure_statuses": post_posting_failure_statuses,
    }
    return load_paginated_data(
        "get",
        "/v1/post-posting-failures",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_post_posting_failures(ids=None) -> Any:
    """
    :param ids: A list of IDs of Post-Posting Failures to be retrieved. Required. Required. Min count: 1. Max count: 50.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/post-posting-failures:batchGet", query_params)


def list_posting_instruction_batches(
    all_pages=True,
    account_ids=None,
    client_batch_ids=None,
    payment_device_tokens=None,
    client_transaction_ids=None,
    page_size=100,
    order_by_direction=None,
    start_time=None,
    end_time=None,
) -> Any:
    """
    :param all_pages: To get the all pages
    :param account_ids: Filters posting instruction batches by the `account_ids` of their
    associated posting instructions. Optional.
    :param client_batch_ids: Filters posting instruction batches by their `client_batch_ids`. Optional.
    :param payment_device_tokens:
    :param client_transaction_ids: Filters posting instruction batches by the `client_transaction_ids` of their
    associated posting instructions. Optional.<br><br>If a matching `client_transaction_id` is used in multiple
    `client_ids`, this may return more than one client transaction.
    :param page_size: The maximum number of results to retrieve. Required; non-zero.
    Required. Min value: 1. Max value: 100.
    :param order_by_direction: The direction to order results in, by `value_timestamp`. Optional.
    :param start_time: Filters posting instruction batches by `value_timestamp`. The earliest posting instruction batch
    returned in the list will have been created after or at `start_time`.
    Optional. Must be formatted as an RFC3339 timestamp.
    :param end_time: Filters posting instruction batches by `value_timestamp`. The latest posting instruction batch
    returned in the list will have been created before `end_time`. Optional. Must be formatted as an RFC3339 timestamp.
    """
    if account_ids is None:
        account_ids = []
    if client_batch_ids is None:
        client_batch_ids = []
    if payment_device_tokens is None:
        payment_device_tokens = []
    if client_transaction_ids is None:
        client_transaction_ids = []
    if order_by_direction is None:
        order_by_direction = ""
    if start_time is None:
        start_time = ""
    if end_time is None:
        end_time = ""

    query_params = {
        "account_ids": account_ids,
        "client_batch_ids": client_batch_ids,
        "payment_device_tokens": payment_device_tokens,
        "client_transaction_ids": client_transaction_ids,
        "order_by_direction": order_by_direction,
        "start_time": start_time,
        "end_time": end_time,
    }
    return load_paginated_data(
        "get",
        "/v1/posting-instruction-batches",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_async_operations(ids=None) -> Any:
    """
    :param ids: The IDs of the AsyncOperations to retrieve.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request(
        "get", "/v1/posting-instruction-batches/async-operations:batchGet", query_params
    )


def get_posting_instruction_batch(id=None) -> Any:
    """
    :param id: The ID of the posting instruction batch to retrieve.
    """
    return send_api_request("get", f"/v1/posting-instruction-batches/{id}")


def batch_get_posting_instruction_batches(ids=None) -> Any:
    """
    :param ids: A list of IDs of posting instruction batches to retrieve. Required; must be non-empty.
    This field must contain a valid UUID in the canonical 8-4-4-4-12 form. Required.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/posting-instruction-batches:batchGet", query_params)


def list_postings_apiclients(all_pages=True, page_size=10) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of results to retrieve. Required; must be non-zero.
    the first page of results will be returned. Optional.
    """

    return load_paginated_data(
        "get", "/v1/postings-api-clients", page_size=page_size, fetch_all_pages=all_pages
    )


def get_postings_apiclient(id=None) -> Any:
    """
    :param id: A unique ID that identifies a `PostingsAPIClient` to the Postings API. Required.
    """
    return send_api_request("get", f"/v1/postings-api-clients/{id}")


def batch_get_postings_apiclients(ids=None) -> Any:
    """
    :param ids: A list of unique IDs that identify `PostingsAPIClient`s to the Postings API. Required.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/postings-api-clients:batchGet", query_params)


def list_processing_groups(all_pages=True, page_size=100) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of Processing Groups to be listed per page. Required. Min value: 1. Max value: 100.
    """

    return load_paginated_data(
        "get", "/v1/processing-groups", page_size=page_size, fetch_all_pages=all_pages
    )


def get_processing_group(id=None) -> Any:
    """
    :param id: The ID of the Processing Group to be retrieved. Required.
    """
    return send_api_request("get", f"/v1/processing-groups/{id}")


def list_product_versions(all_pages=True, product_id=None, view=None, page_size=30) -> Any:
    """
    :param all_pages: To get the all pages
    :param product_id: The product ID that product versions are to be listed for. Required.
    :param view: Indicates which fields should be included in the product versions. Optional.
    :param page_size: Required. Min value: 1. Max value: 30.
    """
    if product_id is None:
        product_id = ""
    if view is None:
        view = ""

    query_params = {
        "product_id": product_id,
        "view": view,
    }
    return load_paginated_data(
        "get", "/v1/product-versions", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def list_product_version_parameters_timeseries(product_version_id=None) -> Any:
    """
    :param product_version_id: The product version ID the parameter timeseries is to be retrieved for.
    """
    return send_api_request("get", f"/v1/product-versions/{product_version_id}:paramTimeseries")


def batch_get_product_versions(ids=None, view=None) -> Any:
    """
    :param ids: A list of the IDs of the product versions to be retrieved. Required; must be non-empty.
    :param view: Indicates which fields should be included for the product versions. Optional; default is basic view.
    """
    if ids is None:
        ids = []
    if view is None:
        view = ""

    query_params = {
        "ids": ids,
        "view": view,
    }
    return send_api_request("get", "/v1/product-versions:batchGet", query_params)


def list_products(all_pages=True, include_internality=None, page_size=30) -> Any:
    """
    :param all_pages: To get the all pages
    :param include_internality: Whether to include internal and/or external Products in the results.
    :param page_size: Required. Min value: 1. Max value: 30.
    """
    if include_internality is None:
        include_internality = ""

    query_params = {
        "include_internality": include_internality,
    }
    return load_paginated_data(
        "get", "/v1/products", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_products(ids=None) -> Any:
    """
    :param ids: The list of product IDs for the products that are to be retrieved. Required; must be non-empty.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/products:batchGet", query_params)


def list_restriction_set_definition_versions(
    exclude_previous_versions=None, restriction_set_definition_id=None
) -> Any:
    """
    :param exclude_previous_versions: Indicates if previous versions should be excluded. Optional; default false.
    :param restriction_set_definition_id: The restriction set definition ID that the restriction set definition
    versions must belong to. If empty, all restriction set definitions are returned. Optional for GRPC requests.
    """
    if exclude_previous_versions is None:
        exclude_previous_versions = False
    if restriction_set_definition_id is None:
        restriction_set_definition_id = ""

    query_params = {
        "exclude_previous_versions": exclude_previous_versions,
        "restriction_set_definition_id": restriction_set_definition_id,
    }
    return send_api_request("get", "/v1/restriction-set-definition-versions", query_params)


def batch_get_restriction_set_definition_versions(ids=None) -> Any:
    """
    :param ids: A list of the IDs of restriction set definition versions that are to be retrieved.
    Required; must be non-empty. The 6.0 release will enforce a maximum number of IDs of 50. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/restriction-set-definition-versions:batchGet", query_params)


def list_restriction_set_definition_versions2(
    restriction_set_definition_id=None, exclude_previous_versions=None
) -> Any:
    """
    :param restriction_set_definition_id: The restriction set definition ID that the restriction
    set definition versions must belong to. If empty, all restriction set definitions are returned.
    Optional for GRPC requests.
    :param exclude_previous_versions: Indicates if previous versions should be excluded. Optional; default false.
    """
    if exclude_previous_versions is None:
        exclude_previous_versions = False

    query_params = {
        "exclude_previous_versions": exclude_previous_versions,
    }
    return send_api_request(
        "get",
        f"/v1/restriction-set-definition/{restriction_set_definition_id}/versions",
        query_params,
    )


def list_restriction_set_definitions(all_pages=True, page_size=500) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of results to be retrieved. Required; non-zero; maximum 500.
    Required. Min value: 1. Max value: 500.
    """

    return load_paginated_data(
        "get", "/v1/restriction-set-definitions", page_size=page_size, fetch_all_pages=all_pages
    )


def list_restriction_sets(
    effective_timestamp=None, customer_ids=None, account_ids=None, payment_device_ids=None
) -> Any:
    """
    :param effective_timestamp: The time at which restriction sets apply.
    Any restriction sets that are not yet active or have already expired at this time will be excluded. Optional;
    default is current time. Must be formatted as an RFC3339 timestamp.
    :param customer_ids: The IDs of customers that restriction sets are applied to.
    Optional; Boolean OR interaction with other fields.
    :param account_ids: The IDs of accounts that restriction sets are applied to.
    Optional; Boolean OR interaction with other fields.
    :param payment_device_ids: The IDs of payment devices that restriction sets are applied to.
    Optional; Boolean OR interaction with other fields.
    """
    if effective_timestamp is None:
        effective_timestamp = ""
    if customer_ids is None:
        customer_ids = []
    if account_ids is None:
        account_ids = []
    if payment_device_ids is None:
        payment_device_ids = []

    query_params = {
        "effective_timestamp": effective_timestamp,
        "customer_ids": customer_ids,
        "account_ids": account_ids,
        "payment_device_ids": payment_device_ids,
    }
    return send_api_request("get", "/v1/restriction-sets", query_params)


def batch_get_restriction_sets(ids=None) -> Any:
    """
    :param ids: A list of the IDs of restriction sets that are to be retrieved. Required;
    must be non-empty. The 6.0 release will enforce a maximum number of IDs of 50. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/restriction-sets:batchGet", query_params)


def list_restrictions(
    effective_timestamp=None, customer_ids=None, account_ids=None, payment_device_ids=None
) -> Any:
    """
    :param effective_timestamp: The time at which restrictions apply. Any restrictions that are not yet active or
    have already expired at this time will be excluded. Optional; default is current time.
    Must be formatted as an RFC3339 timestamp.
    :param customer_ids: The IDs of customers that restrictions are applied to.
    Optional; Boolean OR interaction with other fields.
    :param account_ids: The IDs of accounts that restrictions are applied to.
    Optional; Boolean OR interaction with other fields.
    :param payment_device_ids: The IDs of payment devices that restrictions are applied to.
    Optional; Boolean OR interaction with other fields.
    """
    if effective_timestamp is None:
        effective_timestamp = ""
    if customer_ids is None:
        customer_ids = []
    if account_ids is None:
        account_ids = []
    if payment_device_ids is None:
        payment_device_ids = []

    query_params = {
        "effective_timestamp": effective_timestamp,
        "customer_ids": customer_ids,
        "account_ids": account_ids,
        "payment_device_ids": payment_device_ids,
    }
    return send_api_request("get", "/v1/restrictions", query_params)


def list_jobs(
    all_pages=True,
    schedule_id=None,
    schedule_ids=None,
    status=None,
    from_timestamp=None,
    to_timestamp=None,
    page_size=500,
) -> Any:
    """
    :param all_pages: To get the all pages
    :param schedule_id: The ID of the Schedule used to filter for associated Jobs. At least one of the schedule_id
    or status fields must be populated.
    :param schedule_ids: List of Schedule IDs used to filter for associated jobs. At least one of the schedule_ids
    or status fields must be populated. Max length: 50 characters.
    :param status: Filter for jobs that have this status. At least one of the schedule_ids or status fields must be
    populated.
    :param from_timestamp: Scheduled_timestamp used to list all Jobs with a scheduled_timestamp
    equal to or after this time. Optional.
    :param to_timestamp: Scheduled_timestamp used to list all Jobs with a scheduled_timestamp equal to or before this
    time. Optional.
    :param page_size: The number of results to be listed. Required. Min value: 1. Max value: 500.
    """
    if schedule_id is None:
        schedule_id = ""
    if schedule_ids is None:
        schedule_ids = []
    if status is None:
        status = ""
    if from_timestamp is None:
        from_timestamp = ""
    if to_timestamp is None:
        to_timestamp = ""

    query_params = {
        "schedule_id": schedule_id,
        "schedule_ids": schedule_ids,
        "status": status,
        "from_timestamp": from_timestamp,
        "to_timestamp": to_timestamp,
    }
    return load_paginated_data(
        "get", "/v1/jobs", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_jobs(ids=None) -> Any:
    """
    :param ids: The Job or Jobs to be retrieved using their Job IDs. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/jobs:batchGet", query_params)


def list_schedules(
    all_pages=True, page_size=500, status=None, name_filter=None, resource=None
) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of results to be listed. Required; must be non-zero. Required.
    Min value: 1. Max value: 500.
    :param status:
    :param name_filter: Filter schedules by those whose name starts with this prefix.
     Cannot be used with resource filter. Optional.
    :param resource:
    """
    if status is None:
        status = ""
    if name_filter is None:
        name_filter = ""
    if resource is None:
        resource = None

    query_params = {
        "status": status,
        "name_filter": name_filter,
        "resource": resource,
    }
    return load_paginated_data(
        "get", "/v1/schedules", query_params, page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_schedules(ids=None) -> Any:
    """
    :param ids: Maps the Schedule ID to the requested Schedules. Required. Min count: 1.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/schedules:batchGet", query_params)


def list_supervisor_contract_versions(
    all_pages=True, supervisor_contract_id=None, fields_to_include=None, page_size=50
) -> Any:
    """
    :param all_pages: To get the all pages
    :param supervisor_contract_id: The Supervisor Contract ID to retrieve values for. Required.
    :param fields_to_include: Additional fields to return; optional. Some Supervisor Contract Version fields are
    omitted by default as they are bulky or costly; if those fields are specified here, they will be populated
    in the response.
    :param page_size: The number of Supervisor Contract Versions to be retrieved. Required. Min value: 1. Max value: 50.
    """
    if supervisor_contract_id is None:
        supervisor_contract_id = ""
    if fields_to_include is None:
        fields_to_include = []

    query_params = {
        "supervisor_contract_id": supervisor_contract_id,
        "fields_to_include": fields_to_include,
    }
    return load_paginated_data(
        "get",
        "/v1/supervisor-contract-versions",
        query_params,
        page_size=page_size,
        fetch_all_pages=all_pages,
    )


def batch_get_supervisor_contract_versions(ids=None, fields_to_include=None) -> Any:
    """
    :param ids: List of IDs of the Supervisor Contract Versions to retrieve.
    :param fields_to_include: Additional fields to return; optional. Some Supervisor Contract Version fields are
    omitted by default as they are bulky or costly; if those fields are specified here, they will be populated
    in the response.
    """
    if ids is None:
        ids = []
    if fields_to_include is None:
        fields_to_include = []

    query_params = {
        "ids": ids,
        "fields_to_include": fields_to_include,
    }
    return send_api_request("get", "/v1/supervisor-contract-versions:batchGet", query_params)


def list_supervisor_contracts(all_pages=True, page_size=50) -> Any:
    """
    :param all_pages: To get the all pages
    :param page_size: The number of Supervisor Contracts to be retrieved. Required. Min value: 1. Max value: 50.
    """

    return load_paginated_data(
        "get", "/v1/supervisor-contracts", page_size=page_size, fetch_all_pages=all_pages
    )


def batch_get_supervisor_contracts(ids=None) -> Any:
    """
    :param ids: List of IDs of the Supervisor Contracts to retrieve.
    """
    if ids is None:
        ids = []

    query_params = {
        "ids": ids,
    }
    return send_api_request("get", "/v1/supervisor-contracts:batchGet", query_params)


def get_vault_version() -> Any:
    return send_api_request("get", "/v1/vault-version")
