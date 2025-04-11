import json
from typing import List, Any
from uuid import uuid4
from tools.pipeline_tools.common.api_helpers import (fetch_all_pages, make_api_call)


def get_all_customers(status=None, page_size=200, all_pages=True):
    parameters = {}
    if status is not None:
        parameters = {
            "statuses": [status],
        }

    return fetch_all_pages("get", "/v1/customers", parameters, page_size, all_pages)


def get_account_info(account_id, parameters=None):
    return make_api_call("get", f"/v1/accounts/{account_id}", parameters)


def modify_product_parameter(
    product_version_id: str, items_to_add=None, items_to_remove=None, request_id=""
) -> dict[str, str]:
    if items_to_add is None:
        items_to_add = []
    if items_to_remove is None:
        items_to_remove = []
    request_id = request_id or str(uuid4())
    items_data = {
        "request_id": request_id,
        "items_to_add": items_to_add,
        "items_to_remove": items_to_remove,
    }
    response = make_api_call(
        "put",
        f"/v1/product-versions/{product_version_id}:updateparameters",
        data=json.dumps(items_data),
    )

    return response


def get_param_timeseries_by_product_version(product_version_id) -> List[Any]:
    return make_api_call("get", f"/v1/product-versions/{product_version_id}:paramTimeseries")


def get_account_param_timeseries(account_id) -> List[Any]:
    return make_api_call("get", f"/v1/accounts/{account_id}:paramTimeseries")


def get_all_products(
    include_internality="INTERNALITY_REFINER_EXTERNAL", page_size=10, all_pages=True
):
    parameters = {
        "include_internality": include_internality,
    }

    return fetch_all_pages("get", "/v1/products", parameters, page_size, all_pages)


def get_multiple_product_versions(product_version_id, include_parameters=False) -> List[Any]:
    parameters = {
        "ids": product_version_id,
    }
    if include_parameters:
        parameters["view"] = "PRODUCT_VERSION_VIEW_INCLUDE_PARAMETERS"

    return make_api_call("get", "/v1/product-versions:batchGet", parameters)


def get_all_product_versions(
    product_id, include_parameters=False, page_size=10, all_pages=True
) -> List[Any]:
    parameters = {
        "product_id": product_id,
    }
    if include_parameters:
        parameters["view"] = "PRODUCT_VERSION_VIEW_INCLUDE_PARAMETERS"

    return fetch_all_pages("get", "/v1/product-versions", parameters, page_size, all_pages)


def get_all_accounts(
    account_statuses=None,
    product_version_ids=None,
    opening_timestamp_from=None,
    opening_timestamp_to=None,
    page_size=100,
    all_pages=True,
) -> List[Any]:
    if account_statuses is None:
        account_statuses = ["ACCOUNT_STATUS_OPEN", "ACCOUNT_STATUS_PENDING_CLOSURE"]
    if product_version_ids is None:
        product_version_ids = []
    parameters = {"account_statuses": account_statuses, "product_version_ids": product_version_ids}
    if opening_timestamp_from is not None:
        parameters.update({"opening_timestamp_range.from": opening_timestamp_from})
    if opening_timestamp_to is not None:
        parameters.update({"opening_timestamp_range.to": opening_timestamp_to})

    return fetch_all_pages("get", "/v1/accounts", parameters, page_size, all_pages)


def get_live_balances(account_id, account_address=None, page_size=100, all_pages=True) -> List[Any]:
    parameters = {
        "account_ids": account_id,
    }
    if account_address is not None:
        parameters.update({"account_addresses": account_address})

    return fetch_all_pages("get", "/v1/balances/live", parameters, page_size, all_pages)


def get_account_updates(account_id: str, page_size=100, all_pages=True) -> List[Any]:
    parameters = {
        "account_id": account_id,
    }

    return fetch_all_pages("get", "/v1/account-updates", parameters, page_size, all_pages)


def migrate_account_data(
    account_id,
    product_version_id,
    schedule_migration_type="SCHEDULE_MIGRATION_TYPE_PRESERVE_SCHEDULES_IF_NO_GROUP_CHANGES",
    request_id="",
):
    request_id = request_id or str(uuid4())
    migration_payload = {
        "request_id": request_id,
        "account_update": {
            "account_id": account_id,
            "product_version_update": {
                "product_version_id": product_version_id,
                "schedule_migration_type": schedule_migration_type,
            },
        },
    }
    response = make_api_call("post", "/v1/account-updates", data=json.dumps(migration_payload))

    return response


def migrate_account_between_products(
    from_product_version_id,
    to_product_version_id,
    schedule_migration_type="SCHEDULE_MIGRATION_TYPE_RECREATE_ALL_SCHEDULES_AND_GROUPS",
    request_id="",
):
    request_id = request_id or str(uuid4())
    migration_payload = {
        "request_id": request_id,
        "account_migration": {
            "product_version_migration": {
                "from_product_version_ids": [from_product_version_id],
                "to_product_version_id": to_product_version_id,
                "schedule_migration_type": schedule_migration_type,
            }
        },
    }
    response = make_api_call("post", "/v1/account-migrations", data=json.dumps(migration_payload))

    return response


def get_account_migrations_by_id(account_migration_id: str):
    parameters = {"ids": account_migration_id}
    response = make_api_call(
        "get",
        "/v1/account-migrations:batchGet",
        parameters,
    )

    return response


def activate_account(account_id, request_id=""):
    request_id = request_id or str(uuid4())
    update_payload = {
        "request_id": request_id,
        "account_update": {"account_id": account_id, "activation_update": {}},
    }
    response = make_api_call("post", "/v1/account-updates", data=json.dumps(update_payload))

    return response


def update_account_closure(account_id, request_id=""):
    request_id = request_id or str(uuid4())
    update_payload = {
        "request_id": request_id,
        "account_update": {"account_id": account_id, "closure_update": {}},
    }
    response = make_api_call("post", "/v1/account-updates", data=json.dumps(update_payload))

    return response


def update_account_instance_fields(account_id, instance_jdata, request_id=""):
    request_id = request_id or str(uuid4())
    update_payload = {
        "request_id": request_id,
        "account_update": {
            "account_id": account_id,
            "instance_param_vals_update": {"instance_param_vals": instance_jdata},
        },
    }
    response = make_api_call("post", "/v1/account-updates", data=json.dumps(update_payload))

    return response


def get_all_schedules(
    status="SCHEDULE_STATUS_FAILED", page_size=100, all_pages=True, name_filter=None
):
    parameters = {}
    if status:
        parameters.update({"status": status})
    if name_filter:
        parameters.update({"name_filter": name_filter})

    return fetch_all_pages("get", "/v1/schedules", parameters, page_size, all_pages)


def get_account_schedule_mappings(account_id, page_size=100, all_pages=True):
    parameters = {"account_id": account_id}

    return fetch_all_pages("get", "/v1/account-schedule-assocs", parameters, page_size, all_pages)


def get_schedules_by_ids(schedule_ids):
    schedule_id_param = ""
    for schedule_id in schedule_ids:
        schedule_id_param += "ids=" + schedule_id + "&"

    return make_api_call("get", "/v1/schedules:batchGet?" + schedule_id_param)


def get_all_jobs(sched_id, page_size=10, all_pages=True):
    parameters = {"schedule_id": sched_id}

    return fetch_all_pages("get", "/v1/jobs", parameters, page_size, all_pages)


def get_all_account_schedules(account_id):
    account_schedule_associations = get_account_schedule_mappings(account_id)
    schedule_ids = [item["schedule_id"] for item in account_schedule_associations]

    return get_schedules_by_ids(schedule_ids)


def get_posting_instruction_batches(start_time, end_time, page_size=50, all_pages=True):
    parameters = {"start_time": start_time, "end_time": end_time}

    return fetch_all_pages(
        "get", "/v1/posting-instruction-batches", parameters, page_size, all_pages
    )


def get_posting_instruction_batch_by_client_id(client_batch_id, page_size=50, all_pages=True):
    parameters = {"client_batch_ids": client_batch_id}

    return fetch_all_pages(
        "get", "/v1/posting-instruction-batches", parameters, page_size, all_pages
    )


def get_posting_instruction_batch_by_account_id(
    account_ids, posting_start_time, posting_end_time, page_size=100, all_pages=True
):
    parameters = {
        "account_ids": account_ids,
        "order_by_direction": "ORDER_BY_ASC",
        "start_time": posting_start_time,
        "end_time": posting_end_time,
    }

    return fetch_all_pages(
        "get", "/v1/posting-instruction-batches", parameters, page_size, all_pages
    )


def get_post_posting_failure_logs(page_size=50, all_pages=True):
    parameters = {}

    return fetch_all_pages("get", "/v1/post-posting-failures", parameters, page_size, all_pages)


def republish_failed__post_postings(
    account_id, republish_type="REPUBLISH_TYPE_REPUBLISH_SINGLE_FAILURE"
):
    data = {"account_id": account_id, "republish_type": republish_type}

    return make_api_call(
        method="post", path="/v1/post-posting-failures:republish", data=json.dumps(data)
    )


def republish_existing_job(job_id):
    response = make_api_call("post", f"/v1/jobs/{job_id}:republish")

    return response


def list_service_accounts_by_status(status, page_size=50, all_pages=True):
    parameters = {"service_account_statuses": status}

    return fetch_all_pages("get", "/v1/service-accounts", parameters, page_size, all_pages)


def create_service_account(sa_data, request_id=""):
    request_id = request_id or str(uuid4())
    service_account_payload = {
        "request_id": request_id,
        "service_account": {"name": sa_data["name"], "permissions": sa_data["permissions_to_add"]},
    }
    response = make_api_call(
        "post", "/v1/service-accounts", data=json.dumps(service_account_payload)
    )

    return response


def update_service_account_permissions(update_sa_data, request_id=""):
    request_id = request_id or str(uuid4())
    service_account_payload = {
        "request_id": request_id,
        "items_to_add": update_sa_data["permissions_to_add"],
        "items_to_remove": update_sa_data["permissions_to_remove"],
    }
    response = make_api_call(
        "put",
        f'/v1/service-accounts/{update_sa_data["id"]}:updatePermissions',
        data=json.dumps(service_account_payload),
    )
    return response


def async_create_posting_instruction_batches(req_pib):
    pib_payload = req_pib
    response = make_api_call(
        "post", "/v1/posting-instruction-batches:asyncCreate", data=json.dumps(pib_payload)
    )

    return response


def update_account_details(account_id, parameters=None):
    return make_api_call("put", f"/v1/accounts/{account_id}", data=json.dumps(parameters))


def get_linked_payment_devices(account_id):
    parameters = {"account_ids": account_id, "include_inactive": "false"}

    return fetch_all_pages("get", "/v1/payment-device-links", parameters)


def disable_payment_device_link(payment_device_link_id):
    update_payload = {
        "payment_device_link": {"status": "PAYMENT_DEVICE_LINK_STATUS_INACTIVE"},
        "request_id": str(uuid4()),
        "update_mask": {
            "paths": [
                "status",
            ]
        },
    }
    response = make_api_call(
        "put", f"/v1/payment-device-links/{payment_device_link_id}", data=json.dumps(update_payload)
    )

    return response