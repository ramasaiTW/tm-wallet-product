from . import exceptions as exceptions, symbols as symbols
from abc import ABC
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

class StrictInterface(ABC):

    def __new__(cls, *args, **kwargs):
        ...

class TypeQualifier:

    def __init__(self, optional: bool=..., repeated: bool=..., deprecated: bool=..., description: Optional[str]=...) -> None:
        ...

    def make_spec(self) -> Dict[str, Any]:
        ...

class TypeFixed(TypeQualifier):

    def __init__(self, name: str, *, optional: bool=..., repeated: bool=..., deprecated: bool=..., description: Optional[str]=...) -> None:
        ...

    def check(self, owner_str: str, type_registry: Any, value: Optional[List[Any]]):
        ...

    def make_docstring(self, key: str):
        ...

    def make_type_docstring(self):
        ...

def TypedList(item_type: type):
    ...

def TypedDefaultDict(dict_type: type):
    ...

class NativeObjectSpec:
    name: str
    object: Any
    package: Optional[Any]
    docs: Optional[str]
    description: str

    def __init__(self, name: str, object: Any, *, package: Optional[Any]=..., docs: Optional[str]=..., description: str=...) -> None:
        ...

class ValueSpec:
    name: str
    docstring: str
    type: str

    def __init__(self, name: str, type: str, docstring: str) -> None:
        ...

class FixedValueSpec:
    name: str
    docstring: str
    fixed_value: Any
    type: str

    def __init__(self, name: str, type: str, fixed_value: Any, docstring: str) -> None:
        ...

class ReturnValueSpec:
    docstring: str
    type: str

    def __init__(self, type: str, docstring: str) -> None:
        ...

class EnumSpec:
    name: str
    docstring: str
    members: List[Any]
    show_values: bool

    def __init__(self, name: str, docstring: str, members: List[Any], *, show_values: bool=...) -> None:
        ...

class Example:
    title: str
    code: str

    def __init__(self, title: str, code: str) -> None:
        ...

class MethodSpec:
    name: str
    docstring: str
    args: List[ValueSpec]
    return_value: Optional[Union[ReturnValueSpec, ValueSpec]]
    examples: List[Example]

    def __init__(self, name: str, docstring: str, *, args: List[ValueSpec]=..., return_value: Optional[Union[ReturnValueSpec, ValueSpec]]=..., examples: List[Example]=...) -> None:
        ...

    def assert_args(self, type_registry: Any, cls_name, args: Dict[str, ValueSpec]):
        ...

    def arg_names(self):
        ...

class ExceptionSpec:
    name: str
    docstring: str
    constructor_args: List[ValueSpec]

    def __init__(self, name: str, docstring: str, constructor_args: List[ValueSpec]=...) -> None:
        ...

class ConstructorSpec(MethodSpec):
    docstring: str
    args: List[ValueSpec]

    def __init__(self, docstring: str, args: List[ValueSpec]) -> None:
        ...

    def assert_args(self, type_registry: Any, cls_name: str, args: Dict[str, ValueSpec]):
        ...

class ClassSpec:
    name: str
    docstring: str
    public_attributes: Optional[List[ValueSpec]]
    constructor: Optional[Any]
    public_methods: Optional[List[MethodSpec]]

    def __init__(self, name: str, docstring: str, *, public_attributes: Optional[List[ValueSpec]]=..., constructor: Optional[Any]=..., public_methods: Optional[List[MethodSpec]]=...) -> None:
        ...

    def assert_constructor_args(self, type_registry, method_args) -> None:
        ...

    def assert_method_args(self, type_registry, method_name, method_args) -> None:
        ...

    def assert_attribute_value(self, type_registry, name, value) -> None:
        ...

class DecoratorSpec:
    name: Any
    object: Any
    docstring: str
    args: Any | None
    smart_contract_args: Any | None
    supervisor_args: Any | None

    def __init__(self, name, object, *, docstring: str=..., args: Any | None=..., smart_contract_args: Any | None=..., supervisor_args: Any | None=...) -> None:
        ...

    def __call__(self, *args, **kwargs):
        ...

class _IntWithValueProperty(int):

    @property
    def value(self):
        ...

class _StrWithValueProperty(str):

    @property
    def value(self):
        ...

def Enum(name: str, key_value_dict: Dict[str, Any], *, docstring: Optional[str]=..., show_values: bool=...) -> type:
    ...

def Timeseries(_item_type, _item_desc, _return_on_empty: Any | None=...):
    ...

def merge_class_specs(derived_spec: ClassSpec, base_spec: ClassSpec) -> ClassSpec:
    ...

def transform_const_enum(name: str, const_enum: Any, *, docstring: str=..., show_values: bool=..., hide_keys: Tuple=...) -> type:
    ...

class _EnumMember:
    name: Any
    value: Any

    def __init__(self, name, value) -> None:
        ...

    def __getitem__(self, key):
        ...

def enum_members(cls):
    ...

class EnumRepr:
    ...

def make_docstring(names: List[str]) -> str:
    ...

def make_docstring_seq(name: str) -> str:
    ...

def dedent_and_strip(string: str) -> str:
    ...

def get_iterator(items: Iterable, hint: str, name, check_empty: bool=...):
    ...

def validate_type(item: Any, expected: Any, *, check_empty: bool=..., is_optional: bool=..., hint: Optional[str]=..., prefix: Optional[str]=...):
    ...