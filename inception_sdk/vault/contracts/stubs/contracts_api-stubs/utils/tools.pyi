from .types_registry import make_contract_version_sandbox as make_contract_version_sandbox
from types import FunctionType
from typing import Any, Dict, List
from unittest import TestCase

class ContractsTestCase(TestCase):
    supported_hook_names: List[str]

    @classmethod
    def setUpClass(cls) -> None:
        ...

    @staticmethod
    def load_contract_code(filepath: str) -> str:
        ...

    def create_sandbox(self, types: Dict[str, Any]) -> Dict[str, Any]:
        ...

    def create_sandbox_with_imports(self, types: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        ...

    def run_contract_function(self, contract_code: str, function_name: str, *args, **kwargs) -> FunctionType:
        ...

    def run_contract_function_with_imports(self, contract_code: str, function_name: str, *args, **kwargs) -> FunctionType:
        ...

class SmartContractsTestCase(ContractsTestCase):
    version: str
    executor_type: str
    module_desc: str
    supported_hook_names: Any

    def create_sandbox(self, types: Dict[str, Any]) -> Dict[str, Any]:
        ...
    requires: Any
    fetch_account_data: Any
    vault: Any

    def setUp(self, *args, **kwargs):
        ...

class SupervisorContractsTestCase(ContractsTestCase):
    version: str
    executor_type: str
    module_desc: str
    supervisee_executor_type: str
    supported_hook_names: Any

    def create_sandbox(self, types: Dict[str, Any]) -> Dict[str, Any]:
        ...

    @classmethod
    def setUpClass(cls) -> None:
        ...
    requires: Any
    vault: Any

    def setUp(self, *args, **kwargs):
        ...

    def create_supervisee_vault(self):
        ...

class ContractModulesTestCase(ContractsTestCase):
    version: str
    executor_type: str
    module_desc: str

class SmartContracts300TestCase(SmartContractsTestCase):
    version: str

class SmartContracts310TestCase(SmartContractsTestCase):
    version: str

class SmartContracts320TestCase(SmartContractsTestCase):
    version: str

class SmartContracts330TestCase(SmartContractsTestCase):
    version: str

class SmartContracts340TestCase(SmartContractsTestCase):
    version: str

class SmartContracts350TestCase(SmartContractsTestCase):
    version: str

class SmartContracts360TestCase(SmartContractsTestCase):
    version: str

class SmartContracts370TestCase(SmartContractsTestCase):
    version: str

class SmartContracts380TestCase(SmartContractsTestCase):
    version: str

class SmartContracts390TestCase(SmartContractsTestCase):
    version: str

class SmartContracts3100TestCase(SmartContractsTestCase):
    version: str

class SmartContracts3110TestCase(SmartContractsTestCase):
    version: str

class SmartContracts3120TestCase(SmartContractsTestCase):
    version: str

class SupervisorContracts340TestCase(SupervisorContractsTestCase):
    version: str

class SupervisorContracts350TestCase(SupervisorContractsTestCase):
    version: str

class SupervisorContracts360TestCase(SupervisorContractsTestCase):
    version: str

class SupervisorContracts370TestCase(SupervisorContractsTestCase):
    version: str

class SupervisorContracts380TestCase(SupervisorContractsTestCase):
    version: str

class SupervisorContracts390TestCase(SupervisorContractsTestCase):
    version: str

class SupervisorContracts3100TestCase(SupervisorContractsTestCase):
    version: str

class SupervisorContracts3110TestCase(SupervisorContractsTestCase):
    version: str

class SupervisorContracts3120TestCase(SupervisorContractsTestCase):
    version: str

class ContractModules390TestCase(ContractModulesTestCase):
    version: str

class ContractModules3100TestCase(ContractModulesTestCase):
    version: str

class ContractModules3110TestCase(ContractModulesTestCase):
    version: str

class ContractModules3120TestCase(ContractModulesTestCase):
    version: str