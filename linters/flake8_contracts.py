# standard libs
import ast
from typing import Any, Generator, Type

from linters.flake8.common import SUPERVISOR_TYPES, SmartContractFileType
from linters.flake8.datetime_visitor import DatetimeVisitor
from linters.flake8.empty_hook_visitor import EmptyHookVisitor
from linters.flake8.get_parameter_visitor import GetParameterVisitor
from linters.flake8.list_metadata_visitor import ListMetadataVisitor
from linters.flake8.parameter_display_name_visitor import ParameterDisplayNameVisitor
from linters.flake8.parameter_name_visitor import ParameterNameVisitor
from linters.flake8.pid_visitor import PidVisitor
from linters.flake8.typehint_visitor import TypehintVisitor

# inception sdk
from inception_sdk.vault.contracts.utils import (
    MissingApiMetadata,
    is_module_in_contracts_language_v4,
)

__version__ = "1.0"


class ContractLinter(object):
    name = "flake8_contracts"
    version = __version__

    def __init__(self, tree, filename=""):
        self.tree: ast.Module = tree
        self.filename: str = filename
        self.contract_file_type = self._determine_type()
        self._contract_version = "4"

    def _determine_type(self) -> SmartContractFileType:
        imported_aliases: list[ast.alias] = []

        # We assume a file isn't contract-related if there are no contract imports or hooks.
        # In theory we could have a purely util-based feature file, but this seems rare and most of
        # our rules wouldn't apply anyway.
        for statement in self.tree.body:
            if isinstance(statement, ast.ImportFrom) and statement.module == "contracts_api":
                imported_aliases = statement.names
                break
        else:
            return SmartContractFileType.UNKNOWN

        try:
            is_module_in_contracts_language_v4(self.tree)
        except MissingApiMetadata:
            # Not a contract or supervisor, so assume it's a feature - non contract files that
            # import contracts_api can ignore the errors in flake8 config.
            # We could consider having some unused module-level metadata to demarcate features
            # if that makes things more robust.
            return SmartContractFileType.FEATURE

        # We rely on supervisor-only imports to detect supervisors. This would only fail
        # if a supervisor has no hooks or doesn't return any non-None results in which case it
        # genuinely isn't really a supervisor (yet)
        if any(imported_alias.name in SUPERVISOR_TYPES for imported_alias in imported_aliases):
            return SmartContractFileType.SUPERVISOR_CONTRACT
        else:
            return SmartContractFileType.CONTRACT

    def run(self) -> Generator[tuple[int, int, str, Type[Any]], None, None]:
        # Check if this is looks like a contract file
        if self.contract_file_type is not SmartContractFileType.UNKNOWN:
            # Checks for CTR001
            datetime_visitor = DatetimeVisitor()
            datetime_visitor.visit(self.tree)
            for line, col, msg in datetime_visitor.violations:
                yield line, col, msg, type(self)

            # Checks for CTR002
            list_metadata_visitor = ListMetadataVisitor(self.tree, contract_version=self._contract_version)
            list_metadata_visitor.visit(self.tree)
            for line, col, msg in list_metadata_visitor.violations:
                yield line, col, msg, type(self)

            # Checks for CTR003-4
            typehint_visitor = TypehintVisitor(contract_file_type=self.contract_file_type)
            typehint_visitor.visit(self.tree)
            for line, col, msg in typehint_visitor.violations:
                yield line, col, msg, type(self)

            # Checks for CTR005
            if self.contract_file_type in {
                SmartContractFileType.SUPERVISOR_CONTRACT,
                SmartContractFileType.CONTRACT,
            }:
                empty_hook_visitor = EmptyHookVisitor(contract_file_type=self.contract_file_type)
                empty_hook_visitor.visit(self.tree)
                for line, col, msg in empty_hook_visitor.violations:
                    yield line, col, msg, type(self)

            # Checks for CTR006
            if self.contract_file_type == SmartContractFileType.CONTRACT:
                get_parameter_visitor = GetParameterVisitor()
                get_parameter_visitor.visit(self.tree)
                for line, col, msg in get_parameter_visitor.violations:
                    yield line, col, msg, type(self)

            # Checks for CTR007
            if self._contract_version == "4":
                parameter_name_visitor = ParameterNameVisitor()
                parameter_name_visitor.visit(self.tree)
                for line, col, msg in parameter_name_visitor.violations:
                    yield line, col, msg, type(self)

            # Checks for CTR008
            parameter_display_name_visitor = ParameterDisplayNameVisitor()
            parameter_display_name_visitor.visit(self.tree)
            for line, col, msg in parameter_display_name_visitor.violations:
                yield line, col, msg, type(self)

            # Checks for CTR009
            pid_visitor = PidVisitor()
            pid_visitor.visit(self.tree)
            for line, col, msg in pid_visitor.violations:
                yield line, col, msg, type(self)
