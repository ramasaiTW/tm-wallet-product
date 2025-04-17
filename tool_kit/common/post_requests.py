import json
from typing import List, Any, Dict, Optional
from tool_kit.helpers.core_api_helper import api_request


def create_account_schedule_tag(
    request_id: str = None,
    tag_id: str = None,
    description: str = None,
    sends_scheduled_operation_reports: bool = False,
    schedule_status_override: str = "ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_UNKNOWN",
    override_start_timestamp: str = None,
    override_end_timestamp: str = None,
    test_pause_at_timestamp: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account_schedule_tag": {
            "id": tag_id,
            "description": description,
            "sends_scheduled_operation_reports": sends_scheduled_operation_reports,
            "schedule_status_override": schedule_status_override,
            "schedule_status_override_start_timestamp": override_start_timestamp,
            "schedule_status_override_end_timestamp": override_end_timestamp,
            "test_pause_at_timestamp": test_pause_at_timestamp,
        },
    }
    return api_request("post", "/v1/account-schedule-tags", data=json.dumps(request_body))


def create_account_migration(
    request_id: str = None,
    migration_id: str = None,
    from_product_version_ids: List[str] = None,
    to_product_version_id: str = None,
    schedule_migration_type: str = "SCHEDULE_MIGRATION_TYPE_RECREATE_ALL_SCHEDULES_AND_GROUPS",
) -> List[Any]:
    if from_product_version_ids is None:
        from_product_version_ids = []

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account_migration": {
            "id": migration_id,
            "product_version_migration": {
                "from_product_version_ids": from_product_version_ids,
                "to_product_version_id": to_product_version_id,
                "schedule_migration_type": schedule_migration_type,
            },
        },
    }
    return api_request("post", "/v1/account-migrations", data=json.dumps(request_body))


def create_account_update_batch(
    request_id: Optional[str] = None,
    batch_id: Optional[str] = None,
    account_update_id: Optional[str] = None,
    account_id: Optional[str] = None,
    create_timestamp: Optional[str] = None,
    last_status_update_timestamp: Optional[str] = None,
    account_update_batch_id: Optional[str] = None,
    instance_param_key: Optional[str] = None,
    instance_param_value: Optional[str] = None,
    invalid_account_update_handling_type: str = "INVALID_ACCOUNT_UPDATE_HANDLING_TYPE_FAIL_BATCH",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account_update_batch": {
            "id": batch_id,
            "account_updates": [
                {
                    "id": account_update_id,
                    "account_id": account_id,
                    "create_timestamp": create_timestamp,
                    "last_status_update_timestamp": last_status_update_timestamp,
                    "account_update_batch_id": account_update_batch_id,
                    "instance_param_vals_update": {
                        "instance_param_vals": {instance_param_key: instance_param_value}
                        if instance_param_key is not None
                        else {}
                    },
                }
            ],
        },
        "create_options": {
            "invalid_account_update_handling_type": invalid_account_update_handling_type
        },
    }
    return api_request("post", "/v1/account-update-batches", data=json.dumps(request_body))


def create_account_update(
    request_id: str = None,
    update_id: str = None,
    account_id: str = None,
    instance_param_vals: Optional[Dict[str, Any]] = None,
) -> List[Any]:
    if instance_param_vals is None:
        instance_param_vals = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account_update": {
            "id": update_id,
            "account_id": account_id,
            "instance_param_vals_update": {"instance_param_vals": instance_param_vals},
        },
    }
    return api_request("post", "/v1/account-updates", data=json.dumps(request_body))


def create_account(
    request_id: str = None,
    account_id: str = None,
    product_id: str = None,
    product_version_id: str = None,
    permitted_denominations: Optional[List[str]] = None,
    status: str = "ACCOUNT_STATUS_UNKNOWN",
    opening_timestamp: str = None,
    stakeholder_ids: Optional[List[str]] = None,
    instance_param_vals: Optional[Dict[str, Any]] = None,
    details: Optional[Dict[str, Any]] = None,
) -> List[Any]:
    if permitted_denominations is None:
        permitted_denominations = []
    if stakeholder_ids is None:
        stakeholder_ids = []
    if instance_param_vals is None:
        instance_param_vals = {}
    if details is None:
        details = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account": {
            "id": account_id,
            "product_id": product_id,
            "product_version_id": product_version_id,
            "permitted_denominations": permitted_denominations,
            "status": status,
            "opening_timestamp": opening_timestamp,
            "stakeholder_ids": stakeholder_ids,
            "instance_param_vals": instance_param_vals,
            "details": details,
        },
    }
    return api_request("post", "/v1/accounts", data=json.dumps(request_body))


def create_service_account(
    name: str = None, permissions: Optional[List[str]] = None, request_id: str = None
) -> List[Any]:
    if permissions is None:
        permissions = []

    request_body: Dict[str, Any] = {
        "service_account": {"name": name, "permissions": permissions},
        "request_id": request_id,
    }
    return api_request("post", "/v1/service-accounts", data=json.dumps(request_body))


def create_calendar(
    request_id: str = None,
    calendar_id: str = None,
    calendar_period_descriptor_id: str = None,
    is_active: bool = False,
    create_timestamp: str = None,
    display_name: str = None,
    description: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "calendar": {
            "id": calendar_id,
            "calendar_period_descriptor_id": calendar_period_descriptor_id,
            "is_active": is_active,
            "create_timestamp": create_timestamp,
            "display_name": display_name,
            "description": description,
        },
    }
    return api_request("post", "/v1/calendar", data=json.dumps(request_body))


def create_calendar_event(
    request_id: str = None,
    event_id: str = None,
    calendar_id: str = None,
    name: str = None,
    is_active: bool = False,
    start_timestamp: str = None,
    end_timestamp: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "calendar_event": {
            "id": event_id,
            "calendar_id": calendar_id,
            "name": name,
            "is_active": is_active,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
        },
    }
    return api_request("post", "/v1/calendar-event", data=json.dumps(request_body))


def create_calendar_period_descriptor(
    request_id: str = None,
    descriptor_id: str = None,
    name: str = None,
    start_timestamp: str = None,
    resolution_unit: str = "TIME_UNIT_UNKNOWN",
    resolution_value: int = 0,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "calendar_period_descriptor": {
            "id": descriptor_id,
            "name": name,
            "start_timestamp": start_timestamp,
            "resolution": {"unit": resolution_unit, "value": resolution_value},
        },
    }
    return api_request("post", "/v1/calendar-period-descriptor", data=json.dumps(request_body))


def create_contract_module_version(
    request_id: str = None,
    version_id: str = None,
    contract_module_id: str = None,
    display_name: str = None,
    description: str = None,
    code: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "contract_module_version": {
            "id": version_id,
            "contract_module_id": contract_module_id,
            "display_name": display_name,
            "description": description,
            "code": code,
        },
    }
    return api_request("post", "/v1/contract-module-versions", data=json.dumps(request_body))


def create_contract_module(
    request_id: str = None, module_id: str = None, display_name: str = None, description: str = None
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "contract_module": {
            "id": module_id,
            "display_name": display_name,
            "description": description,
        },
    }
    return api_request("post", "/v1/contract-modules", data=json.dumps(request_body))


def create_smart_contract_module_versions_link(
    request_id: str = None,
    link_id: str = None,
    smart_contract_version_id: str = None,
    alias_to_contract_module_version_id: Optional[Dict[str, str]] = None,
) -> List[Any]:
    if alias_to_contract_module_version_id is None:
        alias_to_contract_module_version_id = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "smart_contract_module_versions_link": {
            "id": link_id,
            "smart_contract_version_id": smart_contract_version_id,
            "alias_to_contract_module_version_id": alias_to_contract_module_version_id,
        },
    }
    return api_request(
        "post", "/v1/smart-contract-module-versions-links", data=json.dumps(request_body)
    )


def simulate_contracts(
    start_timestamp: str = None,
    end_timestamp: str = None,
    smart_contracts: Optional[List[Dict[str, Any]]] = None,
    existing_smart_contracts: Optional[List[Dict[str, Any]]] = None,
    supervisor_contracts: Optional[List[Dict[str, Any]]] = None,
    existing_supervisor_contracts: Optional[List[Dict[str, Any]]] = None,
    contract_modules: Optional[List[Dict[str, Any]]] = None,
    existing_contract_modules: Optional[List[Dict[str, Any]]] = None,
    existing_accounts: Optional[List[Dict[str, Any]]] = None,
    existing_product_data_behaviour: Optional[Dict[str, Any]] = None,
    instructions: Optional[List[Dict[str, Any]]] = None,
    outputs: Optional[List[Dict[str, Any]]] = None,
) -> List[Any]:
    if smart_contracts is None:
        smart_contracts = []
    if existing_smart_contracts is None:
        existing_smart_contracts = []
    if supervisor_contracts is None:
        supervisor_contracts = []
    if existing_supervisor_contracts is None:
        existing_supervisor_contracts = []
    if contract_modules is None:
        contract_modules = []
    if existing_contract_modules is None:
        existing_contract_modules = []
    if existing_accounts is None:
        existing_accounts = []
    if existing_product_data_behaviour is None:
        existing_product_data_behaviour = {"include_all": True, "include_data_types": []}
    if instructions is None:
        instructions = []
    if outputs is None:
        outputs = []

    request_body: Dict[str, Any] = {
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "smart_contracts": smart_contracts,
        "existing_smart_contracts": existing_smart_contracts,
        "supervisor_contracts": supervisor_contracts,
        "existing_supervisor_contracts": existing_supervisor_contracts,
        "contract_modules": contract_modules,
        "existing_contract_modules": existing_contract_modules,
        "existing_accounts": existing_accounts,
        "existing_product_data_behaviour": existing_product_data_behaviour,
        "instructions": instructions,
        "outputs": outputs,
    }
    return api_request("post", "/v1/contracts:simulate", data=json.dumps(request_body))


def create_customer_address(
    request_id: str = None,
    house_name: str = None,
    street_number: str = None,
    street: str = None,
    local_municipality: str = None,
    city: str = None,
    postal_area: str = None,
    governing_district: str = None,
    country: str = None,
    address_type: str = "CUSTOMER_ADDRESS_TYPE_UNKNOWN",
    start_timestamp: str = None,
    end_timestamp: str = None,
    customer_id: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "customer_address": {
            "house_name": house_name,
            "street_number": street_number,
            "street": street,
            "local_municipality": local_municipality,
            "city": city,
            "postal_area": postal_area,
            "governing_district": governing_district,
            "country": country,
            "address_type": address_type,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "customer_id": customer_id,
        },
    }
    return api_request("post", "/v1/customer-addresses", data=json.dumps(request_body))


def create_customer(
    request_id: str = None,
    id: str = None,
    status: str = "CUSTOMER_STATUS_UNKNOWN",
    identifiers: List[Dict[str, str]] = None,
    title: str = None,
    first_name: str = None,
    middle_name: str = None,
    last_name: str = None,
    dob: str = None,
    gender: str = None,
    nationality: str = None,
    email_address: str = None,
    mobile_phone_number: str = None,
    home_phone_number: str = None,
    business_phone_number: str = None,
    contact_method: str = None,
    country_of_residence: str = None,
    country_of_taxation: str = None,
    accessibility: str = None,
    external_customer_id: str = None,
    additional_details: Dict[str, str] = None,
) -> List[Any]:
    if identifiers is None:
        identifiers = []
    if additional_details is None:
        additional_details = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "customer": {
            "id": id,
            "status": status,
            "identifiers": identifiers,
            "customer_details": {
                "title": title,
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "dob": dob,
                "gender": gender,
                "nationality": nationality,
                "email_address": email_address,
                "mobile_phone_number": mobile_phone_number,
                "home_phone_number": home_phone_number,
                "business_phone_number": business_phone_number,
                "contact_method": contact_method,
                "country_of_residence": country_of_residence,
                "country_of_taxation": country_of_taxation,
                "accessibility": accessibility,
                "external_customer_id": external_customer_id,
            },
            "additional_details": additional_details,
        },
    }
    return api_request("post", "/v1/customers", data=json.dumps(request_body))


def search_customers(
    statuses: List[str] = None,
    email_identifiers: List[str] = None,
    phone_identifiers: List[str] = None,
    username_identifiers: List[str] = None,
    external_customer_id_pattern: str = None,
    match_type: str = None,
    page_size: str = None,
    page_token: str = None,
) -> List[Any]:
    if statuses is None:
        statuses = []
    if email_identifiers is None:
        email_identifiers = []
    if phone_identifiers is None:
        phone_identifiers = []
    if username_identifiers is None:
        username_identifiers = []

    request_body: Dict[str, Any] = {
        "statuses": statuses,
        "email_identifiers": email_identifiers,
        "phone_identifiers": phone_identifiers,
        "username_identifiers": username_identifiers,
        "external_customer_id_pattern_match": {
            "pattern": external_customer_id_pattern,
            "match_type": match_type,
        },
        "page_size": page_size,
        "page_token": page_token,
    }
    return api_request("post", "/v1/customers:search", data=json.dumps(request_body))


def replay_journal_events(
    resource_type: str = "RESOURCE_TYPE_UNKNOWN",
    journal_events_to_replay: List[Dict[str, str]] = None,
) -> List[Any]:
    if journal_events_to_replay is None:
        journal_events_to_replay = [{"event_identifier": "value1"}]

    request_body: Dict[str, Any] = {
        "resource_type": resource_type,
        "journal_events_to_replay": journal_events_to_replay,
    }
    return api_request("post", "/v1/journal-events:replay", data=json.dumps(request_body))


def create_flag_definition(
    id: str = None,
    name: str = None,
    description: str = None,
    required_flag_level: str = "FLAG_LEVEL_UNKNOWN",
    flag_visibility: str = "FLAG_VISIBILITY_UNKNOWN",
    request_id: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "flag_definition": {
            "id": id,
            "name": name,
            "description": description,
            "required_flag_level": required_flag_level,
            "flag_visibility": flag_visibility,
        },
        "request_id": request_id,
    }
    return api_request("post", "/v1/flag-definitions", data=json.dumps(request_body))


def create_flag(
    flag_definition_id: str = None,
    description: str = None,
    effective_timestamp: str = None,
    expiry_timestamp: str = None,
    customer_id: str = None,
    request_id: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "flag": {
            "flag_definition_id": flag_definition_id,
            "description": description,
            "effective_timestamp": effective_timestamp,
            "expiry_timestamp": expiry_timestamp,
            "customer_id": customer_id,
        },
        "request_id": request_id,
    }
    return api_request("post", "/v1/flags", data=json.dumps(request_body))


def create_global_parameter_value(
    request_id: str = None,
    global_parameter_id: str = None,
    value: str = None,
    effective_timestamp: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "global_parameter_value": {
            "global_parameter_id": global_parameter_id,
            "value": value,
            "effective_timestamp": effective_timestamp,
        },
    }
    return api_request("post", "/v1/global-parameter-values", data=json.dumps(request_body))


def create_global_parameter(
    request_id: str = None,
    id: str = None,
    display_name: str = None,
    description: str = None,
    value_type: str = "NUMBER_FIELD_DISPLAY_STYLE_NOT_SPECIFIED",
    min_value: str = None,
    max_value: str = None,
    step: str = None,
    initial_value: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "global_parameter": {
            "id": id,
            "display_name": display_name,
            "description": description,
            "number": {
                "value_type": value_type,
                "min_value": min_value,
                "max_value": max_value,
                "step": step,
            },
        },
        "initial_value": initial_value,
    }
    return api_request("post", "/v1/global-parameters", data=json.dumps(request_body))


def create_internal_account(
    request_id: str = None,
    id: str = None,
    product_id: str = None,
    permitted_denominations: List[str] = None,
    details: Dict[str, str] = None,
    tside: str = "TSIDE_UNKNOWN",
) -> List[Any]:
    if permitted_denominations is None:
        permitted_denominations = []
    if details is None:
        details = {}

    request_body: Dict[str, Any] = {
        "internal_account": {
            "id": id,
            "product_id": product_id,
            "permitted_denominations": permitted_denominations,
            "details": details,
            "accounting": {"tside": tside},
        },
        "request_id": request_id,
    }
    return api_request("post", "/v1/internal-accounts", data=json.dumps(request_body))


def create_parameter_value_hierarchy_node(
    request_id: str = None,
    node_id: str = None,
    name: str = None,
    parent_id: str = None,
    metadata: Optional[Dict[str, str]] = None,
) -> List[Any]:
    if metadata is None:
        metadata = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "parameter_value_hierarchy_node": {
            "id": node_id,
            "name": name,
            "parent_id": parent_id,
            "metadata": metadata,
        },
    }
    return api_request("post", "/v1/parameter-value-hierarchy-nodes", data=json.dumps(request_body))


def create_parameter_value(
    request_id: str = None,
    parameter_id: str = None,
    effective_from_timestamp: str = None,
    is_backdated: bool = False,
    string_value: str = None,
    account_config_group_id: str = None,
    account_id: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "parameter_value": {
            "parameter_id": parameter_id,
            "effective_from_timestamp": effective_from_timestamp,
            "is_backdated": is_backdated,
            "value": {"string_value": string_value},
            "account_config_group_id": account_config_group_id,
            "account_id": account_id,
        },
    }
    return api_request("post", "/v1/parameter-values", data=json.dumps(request_body))


def batch_create_parameter_values(
    request_id: str = None,
    parameter_id: str = None,
    effective_from_timestamp: str = None,
    is_backdated: bool = False,
    string_value: str = None,
    account_config_group_id: str = None,
    account_id: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "parameter_values": [
            {
                "parameter_id": parameter_id,
                "effective_from_timestamp": effective_from_timestamp,
                "is_backdated": is_backdated,
                "value": {"string_value": string_value},
                "account_config_group_id": account_config_group_id,
                "account_id": account_id,
            }
        ],
    }
    return api_request("post", "/v1/parameter-values:batchCreate", data=json.dumps(request_body))


def create_parameter(
    request_id: str = None,
    parameter_id: str = None,
    min_length: int = 0,
    max_length: int = 0,
    metadata: Dict[str, str] = None,
) -> List[Any]:
    if metadata is None:
        metadata = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "parameter": {
            "id": parameter_id,
            "constraint": {
                "string_constraint": {"min_length": min_length, "max_length": max_length}
            },
            "metadata": metadata,
        },
    }
    return api_request("post", "/v1/parameters", data=json.dumps(request_body))


def create_payment_device_link(
    request_id: str = None,
    id: str = None,
    token: str = None,
    payment_device_id: str = None,
    account_id: str = None,
    status: str = "PAYMENT_DEVICE_LINK_STATUS_UNKNOWN",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "payment_device_link": {
            "id": id,
            "token": token,
            "payment_device_id": payment_device_id,
            "account_id": account_id,
            "status": status,
        },
        "request_id": request_id,
    }

    return api_request("post", "/v1/payment-device-links", data=json.dumps(request_body))


def create_payment_device(
    request_id: str = None,
    id: str = None,
    routing_info: Dict[str, str] = None,
    status: str = "PAYMENT_DEVICE_STATUS_UNKNOWN",
    start_timestamp: str = "",
    end_timestamp: str = "",
    tags: List[str] = None,
) -> List[Any]:
    if routing_info is None:
        routing_info = {}
    if tags is None:
        tags = []

    request_body: Dict[str, Any] = {
        "payment_device": {
            "id": id,
            "routing_info": routing_info,
            "status": status,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "tags": tags,
        },
        "request_id": request_id,
    }
    return api_request("post", "/v1/payment-devices", data=json.dumps(request_body))


def create_plan_migration(
    request_id: str = None,
    id: str = None,
    from_supervisor_contract_version_ids: List[str] = None,
    to_supervisor_contract_version_id: str = None,
    schedule_migration_type: str = "SCHEDULE_MIGRATION_TYPE_RECREATE_ALL_SCHEDULES_AND_GROUPS",
) -> List[Any]:
    if from_supervisor_contract_version_ids is None:
        from_supervisor_contract_version_ids = []

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "plan_migration": {
            "id": id,
            "supervisor_contract_version_migration": {
                "from_supervisor_contract_version_ids": from_supervisor_contract_version_ids,
                "to_supervisor_contract_version_id": to_supervisor_contract_version_id,
                "schedule_migration_type": schedule_migration_type,
            },
        },
    }

    return api_request("post", "/v1/plan-migrations", data=json.dumps(request_body))


def create_plan_update(
    request_id: str = None,
    id: str = None,
    plan_id: str = None,
    job_id: str = None,
    status: str = "PLAN_UPDATE_STATUS_UNKNOWN",
    account_id: str = None,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "plan_update": {
            "id": id,
            "plan_id": plan_id,
            "job_id": job_id,
            "status": status,
            "associate_account_update": {"account_id": account_id},
        },
    }
    return api_request("post", "/v1/plan-updates", data=json.dumps(request_body))


def create_plan() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/plans", data=json.dumps(request_body))


def create_policy() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/policies", data=json.dumps(request_body))


def republish_post_posting_failure() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/post-posting-failures:republish", data=json.dumps(request_body))


def validate_create_posting_instruction_batch_request() -> List[Any]:
    request_body = {}
    return api_request(
        "post", "/v1/create-posting-instruction-batch:validate", data=json.dumps(request_body)
    )


def create_posting_instruction_batch() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/posting-instruction-batches", data=json.dumps(request_body))


def create_posting_instruction_batch_async() -> List[Any]:
    request_body = {}
    return api_request(
        "post", "/v1/posting-instruction-batches:asyncCreate", data=json.dumps(request_body)
    )


def create_postings_apiclient() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/postings-api-clients", data=json.dumps(request_body))


def create_processing_group() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/processing-groups", data=json.dumps(request_body))


def create_product_version() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/product-versions", data=json.dumps(request_body))


def create_restriction_set_definition_version() -> List[Any]:
    request_body = {}
    return api_request(
        "post", "/v1/restriction-set-definition-versions", data=json.dumps(request_body)
    )


def create_restriction_set_definition_version2(
    restriction_set_definition_id=None,
) -> List[Any]:
    return api_request(
        "post",
        f"/v1/restriction-set-definition/{restriction_set_definition_id}/versions",
    )


def create_restriction_set() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/restriction-sets", data=json.dumps(request_body))


def republish_job(id=None) -> List[Any]:
    """
    :param id: The ID of the Job to be republished.
    """
    return api_request("post", f"/v1/jobs/{id}:republish")


def batch_republish_jobs() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/jobs:batchRepublish", data=json.dumps(request_body))


def create_schedule_tag() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/schedule-tags", data=json.dumps(request_body))


def create_supervisor_contract_version() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/supervisor-contract-versions", data=json.dumps(request_body))


def create_supervisor_contract() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/supervisor-contracts", data=json.dumps(request_body))
