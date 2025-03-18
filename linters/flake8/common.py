"""Flake8 plugin that warns of Contract anti-patterns"""

# standard libs
from enum import Enum
from typing import NamedTuple

ErrorType = tuple[int, int, str]

HookSignature = NamedTuple(
    "HookSignature",
    [("argument_types", str), ("return_type", str)],
)


class SmartContractFileType(Enum):
    FEATURE = "FEATURE"
    CONTRACT = "CONTRACT"
    SUPERVISOR_CONTRACT = "SUPERVISOR_CONTRACT"
    UNKNOWN = "UNKNOWN"


SUPERVISOR_TYPES = {
    # Hook arg/result types
    "SupervisorScheduledEventHookResult",
    "SupervisorScheduledEventHookArguments",
    "SupervisorPrePostingHookResult",
    "SupervisorPrePostingHookArguments",
    "SupervisorPostPostingHookResult",
    "SupervisorPostPostingHookArguments",
    "SupervisorConversionHookResult",
    "SupervisorConversionHookArguments",
    "SupervisorActivationHookResult",
    "SupervisorActivationHookArguments",
    # Metadata types
    "SupervisorContractEventType",
    "SupervisedHooks",
    # Directives
    "UpdatePlanEventTypeDirective",
}

## V4
HOOK_FUNCTIONS = {
    "post_parameter_change_hook",
    "pre_posting_hook",
    "derived_parameter_hook",
    "post_posting_hook",
    "activation_hook",
    "deactivation_hook",
    "pre_parameter_change_hook",
    "scheduled_event_hook",
    "conversion_hook",
}

SUPERVISOR_HOOK_FUNCTIONS = {
    "pre_posting_hook",
    "post_posting_hook",
    "activation_hook",
    "scheduled_event_hook",
    "conversion_hook",
}

HOOK_TEMPLATE_TYPEHINT_MAPPING = {
    "activation_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: ActivationHookArguments",
        "ActivationHookResult | None",
    ),
    "conversion_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: ConversionHookArguments",
        "ConversionHookResult | None",
    ),
    "deactivation_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: DeactivationHookArguments",
        "DeactivationHookResult | None",
    ),
    "derived_parameter_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: DerivedParameterHookArguments",
        "DerivedParameterHookResult",
    ),
    "post_parameter_change_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: PostParameterChangeHookArguments",
        "PostParameterChangeHookResult | None",
    ),
    "post_posting_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: PostPostingHookArguments",
        "PostPostingHookResult | None",
    ),
    "pre_parameter_change_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: PreParameterChangeHookArguments",
        "PreParameterChangeHookResult | None",
    ),
    "pre_posting_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: PrePostingHookArguments",
        "PrePostingHookResult | None",
    ),
    "scheduled_event_hook": HookSignature(
        "vault: SmartContractVault, hook_arguments: ScheduledEventHookArguments",
        "ScheduledEventHookResult | None",
    ),
}

SUPERVISOR_HOOK_TEMPLATE_TYPEHINT_MAPPING = {
    "activation_hook": HookSignature(
        "vault: SupervisorContractVault, hook_arguments: SupervisorActivationHookArguments",
        "SupervisorActivationHookResult | None",
    ),
    "conversion_hook": HookSignature(
        "vault: SupervisorContractVault, hook_arguments: SupervisorConversionHookArguments",
        "SupervisorConversionHookResult | None",
    ),
    "post_posting_hook": HookSignature(
        "vault: SupervisorContractVault, hook_arguments: SupervisorPostPostingHookArguments",
        "SupervisorPostPostingHookResult | None",
    ),
    "pre_posting_hook": HookSignature(
        "vault: SupervisorContractVault, hook_arguments: SupervisorPrePostingHookArguments",
        "SupervisorPrePostingHookResult | None",
    ),
    "scheduled_event_hook": HookSignature(
        "vault: SupervisorContractVault, hook_arguments: SupervisorScheduledEventHookArguments",
        "SupervisorScheduledEventHookResult | None",
    ),
}
