import json
from typing import List, Any
from tool_kit.helpers.core_api_helper import api_request


def update_account_schedule_tag(
    account_schedule_tag_id=None,
    request_id=None,
    schedule_status_override=None,
    schedule_status_override_start_timestamp=None,
    schedule_status_override_end_timestamp=None,
    test_pause_at_timestamp=None,
    processing_group_id=None,
    paths=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "account_schedule_tag": {
            "schedule_status_override": schedule_status_override,
            "schedule_status_override_start_timestamp": schedule_status_override_start_timestamp,
            "schedule_status_override_end_timestamp": schedule_status_override_end_timestamp,
            "test_pause_at_timestamp": test_pause_at_timestamp,
            "processing_group_id": processing_group_id,
        },
        "update_mask": {"paths": paths},
    }

    return api_request(
        "put", f"/v1/account-schedule-tags/{account_schedule_tag_id}", data=json.dumps(request_body)
    )


def update_account_migration(
    account_migration_id=None, request_id=None, status=None, paths=None
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "account_migration": {
            "status": status,
        },
        "update_mask": {
            "paths": paths,
        },
    }

    return api_request(
        "put",
        f"/v1/account-migrations/{account_migration_id}",
        data=json.dumps(request_body),
    )


def update_account(
    account_id=None,
    status=None,
    closing_timestamp=None,
    stakeholder_ids=None,
    paths=None,
    restriction_set_ids=None,
    restriction_set_definition_ids=None,
    restriction_set_definition_version_ids=None,
) -> List[Any]:
    request_body = {
        "account_id": account_id,
        "account": {
            "status": status,
            "closing_timestamp": closing_timestamp,
            "stakeholder_ids": stakeholder_ids,
        },
        "update_mask": {
            "paths": paths,
        },
        "overrides": {
            "override_restrictions": {
                "all": all,
                "restriction_set_ids": restriction_set_ids,
                "restriction_set_definition_ids": restriction_set_definition_ids,
                "restriction_set_definition_version_ids": restriction_set_definition_version_ids,
            }
        },
    }

    return api_request(
        "put",
        f"/v1/accounts/{account_id}",
        data=json.dumps(request_body),
    )


def update_account_details(
    request_id=None,
    account_id=None,
    items_to_add=None,
    items_to_remove=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "account_id": account_id,
        "items_to_add": items_to_add,
        "items_to_remove": items_to_remove,
    }

    return api_request(
        "put",
        f"/v1/accounts/{account_id}:updateDetails",
        data=json.dumps(request_body),
    )


def update_service_account(
    service_account_id=None,
    status=None,
    paths=None,
    refresh_token=None,
) -> List[Any]:
    request_body = {
        "service_account.id": service_account_id,
        "service_account": {
            "status": status,
        },
        "update_mask": {
            "paths": paths,
        },
        "token_update_options": {
            "refresh_token": refresh_token,
        },
    }

    return api_request(
        "put",
        f"/v1/service-accounts/{service_account_id}",
        data=json.dumps(request_body),
    )


def update_service_account_permissions(
    request_id=None,
    service_account_id=None,
    items_to_add=None,
    items_to_remove=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "items_to_add": items_to_add,
        "items_to_remove": items_to_remove,
    }

    return api_request(
        "put",
        f"/v1/service-accounts/{service_account_id}:updatePermissions",
        data=json.dumps(request_body),
    )


def update_calendar_event(
    request_id=None,
    calendar_event_id=None,
    name=None,
    is_active=None,
    paths=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "calendar_event": {
            "name": name,
            "is_active": is_active,
        },
        "update_mask": {
            "paths": paths,
        },
    }

    return api_request(
        "put",
        f"/v1/calendar-event/{calendar_event_id}:updateDetails",
        data=json.dumps(request_body),
    )


def update_bookkeeping_date(
    request_id=None,
    calender_id=None,
    date=None,
    paths=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "bookkeeping_date": {
            "date": date,
        },
        "update_mask": {
            "paths": paths,
        },
    }

    return api_request(
        "put",
        f"/v1/calendar/bookkeeping-date/{calender_id}",
        data=json.dumps(request_body),
    )


def change_current_calendar_period(
    request_id=None,
    calendar_id=None,
    action=None,
    action_timestamp=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "action": action,
        "action_timestamp": action_timestamp,
    }

    return api_request(
        "put",
        f"/v1/calendar/{calendar_id}/period/current:change",
        data=json.dumps(request_body),
    )


def update_calendar(
    request_id=None,
    calendar_id=None,
    is_active=None,
    display_name=None,
    description=None,
    paths=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "calendar": {
            "is_active": is_active,
            "display_name": display_name,
            "description": description,
        },
        "update_mask": {
            "paths": paths,
        },
    }

    return api_request(
        "put",
        f"/v1/calendar/{calendar_id}:updateDetails",
        data=json.dumps(request_body),
    )


def update_customer_address(
    request_id=None,
    customer_address_id=None,
    house_name=None,
    street_number=None,
    street=None,
    local_municipality=None,
    city=None,
    postal_area=None,
    governing_district=None,
    country=None,
    address_type=None,
    start_timestamp=None,
    end_timestamp=None,
    paths=None,
) -> List[Any]:
    request_body = {
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
        },
        "update_mask": {
            "paths": paths,
        },
    }

    return api_request(
        "put",
        f"/v1/customer-addresses/{customer_address_id}",
        data=json.dumps(request_body),
    )


def update_customer(
    request_id=None,
    customer_id=None,
    status=None,
    identifiers=None,
    customer_details_title=None,
    customer_details_first_name=None,
    customer_details_middle_name=None,
    customer_details_last_name=None,
    customer_details_dob=None,
    customer_details_gender=None,
    customer_details_nationality=None,
    customer_details_email_address=None,
    customer_details_mobile_phone_number=None,
    customer_details_home_phone_number=None,
    customer_details_business_phone_number=None,
    customer_details_contact_method=None,
    customer_details_country_of_residence=None,
    customer_details_country_of_taxation=None,
    customer_details_accessibility=None,
    customer_details_external_customer_id=None,
    identifiers_type_email=None,
    identifiers_type_username=None,
    identifiers_type_phone=None,
    paths=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "customer": {
            "status": status,
            "identifiers": [
                {"identifier_type": "IDENTIFIER_TYPE_EMAIL", "identifier": identifiers_type_email},
                {
                    "identifier_type": "IDENTIFIER_TYPE_USERNAME",
                    "identifier": identifiers_type_username,
                },
                {"identifier_type": "IDENTIFIER_TYPE_PHONE", "identifier": identifiers_type_phone},
            ],
            "customer_details": {
                "title": customer_details_title,
                "first_name": customer_details_first_name,
                "middle_name": customer_details_middle_name,
                "last_name": customer_details_last_name,
                "dob": customer_details_dob,
                "gender": customer_details_gender,
                "nationality": customer_details_nationality,
                "email_address": customer_details_email_address,
                "mobile_phone_number": customer_details_mobile_phone_number,
                "home_phone_number": customer_details_home_phone_number,
                "business_phone_number": customer_details_business_phone_number,
                "contact_method": customer_details_contact_method,
                "country_of_residence": customer_details_country_of_residence,
                "country_of_taxation": customer_details_country_of_taxation,
                "accessibility": customer_details_accessibility,
                "external_customer_id": customer_details_external_customer_id,
            },
        },
        "update_mask": {
            "paths": paths,
        },
    }

    return api_request(
        "put",
        f"/v1/customers/{customer_id}",
        data=json.dumps(request_body),
    )


def update_customer_additional_details(
    request_id: str = None,
    customer_id: str = None,
    items_to_add: dict = None,
    items_to_remove: list = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "items_to_add": items_to_add,
        "items_to_remove": items_to_remove,
    }

    return api_request(
        "put",
        f"/v1/customers/{customer_id}:updateAdditionalDetails",
        data=json.dumps(request_body),
    )


def update_flag_definition(
    request_id: str = None,
    flag_definition_id: str = None,
    is_active: bool = None,
    paths: list = None,
) -> List[Any]:
    request_body = {
        "flag_definition": {"is_active": is_active},
        "request_id": request_id,
        "update_mask": {"paths": paths},
    }

    return api_request(
        "put", f"/v1/flag-definitions/{flag_definition_id}", data=json.dumps(request_body)
    )


def update_flag(
    flag_id: str = None,
    request_id: str = None,
    description: str = None,
    is_active: bool = None,
    paths: list = None,
) -> List[Any]:
    request_body = {
        "flag": {"description": description, "is_active": is_active},
        "request_id": request_id,
        "update_mask": {"paths": paths},
    }

    return api_request("put", f"/v1/flags/{flag_id}", data=json.dumps(request_body))


def update_parameter_value_hierarchy_node(
    request_id: str = None,
    parameter_value_hierarchy_node_id: str = None,
    name: str = None,
    metadata: dict = None,
    paths: list = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "parameter_value_hierarchy_node": {"name": name, "metadata": metadata},
        "update_mask": {"paths": paths},
    }

    return api_request(
        "put",
        f"/v1/parameter-value-hierarchy-nodes/{parameter_value_hierarchy_node_id}",
        data=json.dumps(request_body),
    )


def update_parameter_value(
    request_id: str = None,
    parameter_value_id: str = None,
    effective_to_timestamp: str = None,
    is_cancelled: bool = None,
    paths: list = None,
    skip_pre_parameter_change_hook: bool = None,
    set_to_now: bool = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "parameter_value": {
            "effective_to_timestamp": effective_to_timestamp,
            "is_cancelled": is_cancelled,
        },
        "update_mask": {"paths": paths},
        "is_cancelled_update_options": {
            "skip_pre_parameter_change_hook": skip_pre_parameter_change_hook
        },
        "effective_to_timestamp_update_options": {"set_to_now": set_to_now},
    }

    return api_request(
        "put", f"/v1/parameter-values/{parameter_value_id}", data=json.dumps(request_body)
    )


def update_payment_device_link(
    payment_device_link_id: str = None,
    request_id: str = None,
    status: str = "PAYMENT_DEVICE_LINK_STATUS_ACTIVE",
    paths: list = None,
) -> List[Any]:
    request_body = {
        "payment_device_link": {"status": status},
        "request_id": request_id,
        "update_mask": {"paths": paths},
    }

    return api_request(
        "put", f"/v1/payment-device-links/{payment_device_link_id}", data=json.dumps(request_body)
    )


def update_payment_device(
    payment_device_id: str = None,
    request_id: str = None,
    status: str = "PAYMENT_DEVICE_STATUS_PENDING",
    paths: list = None,
    restriction_set_ids: list = None,
    restriction_set_definition_ids: list = None,
    restriction_set_definition_version_ids: list = None,
) -> List[Any]:
    request_body = {
        "payment_device": {"status": status},
        "request_id": request_id,
        "update_mask": {"paths": paths},
        "overrides": {
            "override_restrictions": {
                "all": True,
                "restriction_set_ids": restriction_set_ids,
                "restriction_set_definition_ids": restriction_set_definition_ids,
                "restriction_set_definition_version_ids": restriction_set_definition_version_ids,
            }
        },
    }

    return api_request(
        "put", f"/v1/payment-devices/{payment_device_id}", data=json.dumps(request_body)
    )


def update_policy(
    policy_id: str = None,
    request_id: str = None,
    description: str = None,
    rego_source: str = None,
    paths: list = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "policy": {"description": description, "rego_source": rego_source},
        "update_mask": {"paths": paths},
    }

    return api_request("put", f"/v1/policies/{policy_id}", data=json.dumps(request_body))


def update_postings_apiclient(
    postings_api_client_id: str = None,
    request_id: str = None,
    client_id: str = None,
    response_topic: str = None,
    response_topic_low_priority: str = None,
    update_mask_paths: list = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "postings_api_client": {
            "client_id": client_id,
            "response_topic": response_topic
            or "integration.postings_api.domestic_payment_processor_id.response",
            "response_topic_low_priority": response_topic_low_priority
            or "integration.postings_api.domestic_payment_processor_id.low_priority.response",
        },
        "update_mask": {"paths": update_mask_paths or ["response_topic_low_priority"]},
    }

    return api_request(
        "put", f"/v1/postings-api-clients/{postings_api_client_id}", data=json.dumps(request_body)
    )


def update_processing_group(
    processing_group_id: str = None,
    request_id: str = None,
    timezone: str = None,
    status: str = None,
    update_mask_paths: list = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "processing_group": {
            "timezone": timezone,
            "status": status or "PROCESSING_GROUP_STATUS_ACTIVE",
        },
        "update_mask": {"paths": update_mask_paths},
        "minimum_observation_timestamp_update_options": {
            "schedules_observe_balances_at_unpause_time": True
        },
    }

    return api_request(
        "put", f"/v1/processing-groups/{processing_group_id}", data=json.dumps(request_body)
    )


def update_product_version_params(
    product_version_id=None,
    request_id=None,
    name=None,
    value=None,
    effective_timestamp=None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "items_to_add": [
            {
                "name": name,
                "value": value,
                "effective_timestamp": effective_timestamp,
            }
        ],
        "items_to_remove": [
            {
                "name": name,
                "value": value,
                "effective_timestamp": effective_timestamp,
            }
        ],
    }

    return api_request(
        "put",
        f"/v1/product-versions/{product_version_id}:updateParams",
        data=json.dumps(request_body),
    )


def update_restriction_set(
    restriction_set_id: str = None,
    request_id: str = None,
    is_active: bool = True,
    update_mask_paths: list = None,
) -> List[Any]:
    request_body = {
        "restriction_set": {"is_active": is_active},
        "request_id": request_id,
        "update_mask": {"paths": update_mask_paths},
    }

    return api_request(
        "put", f"/v1/restriction-sets/{restriction_set_id}", data=json.dumps(request_body)
    )


def delete_post_posting_failures(pib_id=None) -> List[Any]:
    """
    :param pib_id: The unique identifier for this restriction set.
    """

    return api_request("put", f"/v1/post-posting-failures/{pib_id}")
