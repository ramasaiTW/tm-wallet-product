from .exceptions import InvalidSmartContractError as InvalidSmartContractError, StrongTypingError as StrongTypingError
from .types_utils import ClassSpec as ClassSpec, DecoratorSpec as DecoratorSpec, EnumSpec as EnumSpec, FixedValueSpec as FixedValueSpec, MethodSpec as MethodSpec, NativeObjectSpec as NativeObjectSpec, ValueSpec as ValueSpec
from typing import Any, Dict, List, Optional, TypeVar

class TypeRegistry(dict):
    disable_type_checking: bool

    def __init__(self, builtins: Dict[str, Any], custom: List[Any], *, disable_type_checking: bool=...) -> None:
        ...

    def assert_type_name(self, type_name: str, obj: Any, location: str):
        ...

    @staticmethod
    def is_valid_type(type_obj: Any, obj: Any):
        ...

class RegistrySpecsSanityCheckResults:
    classes_without_constructor_specs: Any
    missing_attributes: Any
    invalid_attributes: Any
    missing_methods: Any
    invalid_methods: Any
    invalid_method_return_values: Any

    def __init__(self) -> None:
        ...

def check_registry_specs_sanity(registry: TypeRegistry, prebuilt_instances: Dict[str, Any]):
    ...

def make_contract_version_sandbox(contract_lib: Any, disable_type_checking: bool=...) -> Dict[str, Any]:
    ...

def make_contract_version_sandbox_with_imports(contract_lib: Any, imported_native_modules: Optional[set]=..., imported_contract_modules: Optional[dict]=..., contracts_api_imports: Optional[set[str]]=..., contracts_api_import_all: Optional[bool]=..., native_modules_import_all: Optional[bool]=...) -> dict[str, Any]:
    ...
DictKeyType = TypeVar('DictKeyType')
DictValueType = TypeVar('DictValueType')
ListItemType = TypeVar('ListItemType')
OptionalItemType = TypeVar('OptionalItemType')

class TypeCheckingAny:
    ...

class _TypeCheckingDict:

    def __getitem__(self, types):
        ...

class _TypeCheckingList:

    def __getitem__(self, type):
        ...

class _TypeCheckingOptional:

    def __getitem__(self, type):
        ...

class _TypeCheckingTupleCls:

    def __getitem__(self, types):
        ...

class _TypeCheckingUnionCls:

    def __getitem__(self, types):
        ...