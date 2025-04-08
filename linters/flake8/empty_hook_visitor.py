# standard libs
import ast

from linters.flake8.common import (
    HOOK_TEMPLATE_TYPEHINT_MAPPING,
    SUPERVISOR_HOOK_TEMPLATE_TYPEHINT_MAPPING,
    ErrorType,
    SmartContractFileType,
)

ERRORS_CTR005 = "CTR005 do not add empty hooks to contracts"


class EmptyHookVisitor(ast.NodeVisitor):
    """
    Raise an error if empty hooks are added to a contract/supervisor contract
    """

    def __init__(self, contract_file_type: SmartContractFileType):
        self.file_type = contract_file_type
        if contract_file_type == SmartContractFileType.CONTRACT:
            self.hook_mapping = HOOK_TEMPLATE_TYPEHINT_MAPPING
        elif contract_file_type == SmartContractFileType.SUPERVISOR_CONTRACT:
            self.hook_mapping = SUPERVISOR_HOOK_TEMPLATE_TYPEHINT_MAPPING
        else:
            raise ValueError("EmptyHookVisitor requires a Contract or Supervisor file")
        self.violations: list[ErrorType] = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # we could optimise and return early for non-contracts/supervisors
        if node.name in self.hook_mapping:
            self._raise_hook_errors(node)
        self.generic_visit(node)

    def _raise_hook_errors(self, node: ast.FunctionDef) -> None:
        error = ERRORS_CTR005
        if len(node.body) == 1 and (isinstance(node.body[0], ast.Pass) or self._is_empty_return(node.body[0])):
            self.violations.append((node.lineno, 0, error))

    def _is_empty_return(self, node: ast.stmt):
        if isinstance(node, ast.Return):
            if isinstance(node.value, ast.Call):
                # this could potentially be expanded to check that the args/keyword args aren't
                # None/empty containers
                return len(node.value.args) == 0 and len(node.value.keywords) == 0
            return node.value is None

        return False
