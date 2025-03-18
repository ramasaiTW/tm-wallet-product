# standard libs
import ast

from linters.flake8.common import (
    HOOK_TEMPLATE_TYPEHINT_MAPPING,
    SUPERVISOR_HOOK_TEMPLATE_TYPEHINT_MAPPING,
    ErrorType,
    SmartContractFileType,
)

ERRORS_CTR003 = "CTR003 Typehints should be used"
ERRORS_CTR004 = f"{ERRORS_CTR003[:5]}4{ERRORS_CTR003[6:]}"


class TypehintVisitor(ast.NodeVisitor):
    """
    Raise an error if typehints are missing
    """

    def __init__(
        self,
        contract_file_type: SmartContractFileType,
    ):
        self.contract_file_type = contract_file_type
        self.violations: list[ErrorType] = []

        self.hook_mapping = (
            HOOK_TEMPLATE_TYPEHINT_MAPPING
            if contract_file_type == SmartContractFileType.CONTRACT
            else SUPERVISOR_HOOK_TEMPLATE_TYPEHINT_MAPPING
        )

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._generate_errors(node)
        self.generic_visit(node)

    def _generate_errors(
        self,
        node: ast.FunctionDef,
    ) -> None:
        # TODO: can we automate the generation of hook typehints?
        # Ensure that hook typehints are correct for smart contracts
        if node.name in self.hook_mapping:
            self._raise_hook_errors(node)

        # Ensure that helper function typehints are provided
        else:
            all_args = node.args.args + node.args.kwonlyargs + node.args.posonlyargs
            error = f"{ERRORS_CTR004} for helper methods"
            for arg in all_args:
                if not arg.annotation:
                    self.violations.append((node.lineno, arg.col_offset, error))
            if node.returns is None:
                return_error = f"{error} - please include return type"
                self.violations.append((node.lineno, node.col_offset, return_error))

    def _raise_hook_errors(self, node: ast.FunctionDef) -> None:
        argument_types, return_type = self.hook_mapping[node.name]
        error = f"{ERRORS_CTR003} for hooks"

        if not self._args_equal(argument_types, node.args.args):
            arg_error = f"{error} - arguments should be '{argument_types}'"
            offset = 0 if len(node.args.args) == 0 else node.args.args[0].col_offset
            self.violations.append((node.lineno, offset, arg_error))

        actual_return = "" if node.returns is None else ast.unparse(node.returns)
        if return_type != actual_return:
            return_error = f"{error} - return type should be '{return_type}'"
            self.violations.append((node.lineno, node.col_offset, return_error))

    @staticmethod
    def _args_equal(expected: str, actual: list[ast.arg]) -> bool:
        actual_str = ", ".join([ast.unparse(a) for a in actual])
        return expected == actual_str
