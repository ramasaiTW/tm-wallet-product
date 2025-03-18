# standard libs
import ast
import unittest
from collections import defaultdict

from linters.flake8.datetime_visitor import ERRORS_CTR001
from linters.flake8.empty_hook_visitor import EmptyHookVisitor
from linters.flake8.get_parameter_visitor import ERRORS_CTR006, ERRORS_CTR006B, GetParameterVisitor
from linters.flake8.list_metadata_visitor import ERRORS_CTR002, ListMetadataVisitor
from linters.flake8.pid_visitor import ERRORS_CTR009, PidVisitor
from linters.flake8.typehint_visitor import ERRORS_CTR003, ERRORS_CTR004
from linters.flake8_contracts import ContractLinter, SmartContractFileType

# inception sdk
from inception_sdk.common.python.file_utils import load_file_contents

SUPERVISOR_FILE = "linters/test/unit/input/dummy_supervisor.py"
NON_CONTRACT_FILE = "linters/test/unit/input/dummy_python.py"
CONTRACT_FILE = "linters/test/unit/input/dummy_contract.py"
FEATURE_FILE = "linters/test/unit/input/dummy_feature.py"
GET_PARAMETER_EXAMPLE_FILE = "linters/test/unit/input/get_parameter_example.py"
PID_EXAMPLE_FILE = "linters/test/unit/input/pid_example.py"


class SupervisorLinterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ast.parse(load_file_contents(SUPERVISOR_FILE))
        cls.linter = ContractLinter(tree)
        cls.outputs = defaultdict(lambda: [])
        for line, col, msg, _ in cls.linter.run():
            cls.outputs[msg[:6]].append({"line": line, "col": col})

    def test_ctr001_datetime_now_utcnow(self):
        ctr001_errors = self.outputs["CTR001"]
        expected_errors = [
            {"line": 43, "col": 10},
            {"line": 44, "col": 13},
        ]
        self.assertListEqual(ctr001_errors, expected_errors)

    def test_ctr002_event_types(self):
        ctr002_errors = self.outputs["CTR002"]
        expected_errors = [
            {"line": 34, "col": 0},  # event_types append
            {"line": 35, "col": 0},  # event_types +=
            {"line": 36, "col": 0},  # event_types list slice
            {"line": 37, "col": 0},  # event_types list slice
            {"line": 37, "col": 16},  # event_types within func
        ]
        self.assertListEqual(ctr002_errors, expected_errors)

    def test_ctr003_4_typehinting(self):
        ctr003_4_errors = self.outputs["CTR003"] + self.outputs["CTR004"]
        expected_errors = [
            {"line": 42, "col": 20},  # hook signature does not match
            {"line": 42, "col": 0},  # hook has no return type
            {"line": 48, "col": 25},  # hook signature does not match
            {"line": 53, "col": 36},  # no argument typehint
            {"line": 53, "col": 0},  # no return
            {"line": 58, "col": 43},  # no argument typehint
            {"line": 58, "col": 0},  # no return
            {"line": 62, "col": 13},  # no argument typehint
            {"line": 62, "col": 0},  # no return
        ]
        self.assertListEqual(ctr003_4_errors, expected_errors)

    def test_ctr006_get_parameter(self):
        ctr006_errors = self.outputs[ERRORS_CTR006] + self.outputs[ERRORS_CTR006B]
        # the GetParameterVisitor check should never run for
        # v4 supervisors, so this should be empty
        expected_errors = []
        self.assertListEqual(ctr006_errors, expected_errors)


class ContractLinterNonContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ast.parse(load_file_contents(NON_CONTRACT_FILE))
        cls.linter = ContractLinter(tree)
        cls.outputs = defaultdict(lambda: [])
        for line, col, msg, _ in cls.linter.run():
            cls.outputs[msg[:6]].append({"line": line, "col": col})

    def test_non_contract_file_ignored_ctr001(self):
        ctr001_errors = self.outputs[ERRORS_CTR001]
        self.assertListEqual(ctr001_errors, [])

    def test_non_contract_file_ignored_ctr002(self):
        ctr002_errors = self.outputs[ERRORS_CTR002]
        self.assertListEqual(ctr002_errors, [])

    def test_non_contract_file_ignored_ctr003_4(self):
        # temporarily exclude helper errors using CTR004
        ctr003_4_errors = self.outputs[ERRORS_CTR003] + self.outputs[ERRORS_CTR004]
        self.assertListEqual(ctr003_4_errors, [])


class ContractLinterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ast.parse(load_file_contents(CONTRACT_FILE))
        cls.linter = ContractLinter(tree)
        cls.outputs = defaultdict(lambda: [])
        for line, col, msg, _ in cls.linter.run():
            cls.outputs[msg[:6]].append({"line": line, "col": col})

    def test_ctr001_datetime_now_utcnow(self):
        ctr001_errors = self.outputs["CTR001"]
        expected_errors = [
            {"line": 71, "col": 10},
            {"line": 72, "col": 13},
            {"line": 80, "col": 10},
            {"line": 81, "col": 13},
        ]
        self.assertListEqual(ctr001_errors, expected_errors)

    def test_ctr002_event_types(self):
        ctr002_errors = self.outputs["CTR002"]
        expected_errors = [
            {"line": 85, "col": 0},  # event_types append
            {"line": 86, "col": 0},  # event_types +=
            {"line": 87, "col": 0},  # event_types list slice
            {"line": 87, "col": 16},  # event_types list slice
            {"line": 92, "col": 4},  # event_types within func
            {"line": 98, "col": 0},  # global_parameters
            {"line": 100, "col": 0},  # parameters
            {"line": 103, "col": 0},  # supported_denoms
            {"line": 106, "col": 0},  # event_types_groups
            {"line": 109, "col": 0},  # contract_module_imports
            {"line": 112, "col": 0},  # data_fetchers
        ]
        self.assertListEqual(ctr002_errors, expected_errors)

    def test_ctr003_4_typehinting(self):
        ctr003_4_errors = self.outputs["CTR003"] + self.outputs["CTR004"]
        expected_errors = [
            {"line": 116, "col": 31},  # no return
            {"line": 116, "col": 0},  # no vault/argument typehint
            {"line": 122, "col": 47},  # no return
            {"line": 122, "col": 0},  # no argument typehint
            {"line": 127, "col": 54},  # no argument typehint
            {"line": 132, "col": 24},  # no typehint after *
        ]
        self.assertListEqual(ctr003_4_errors, expected_errors)

    def test_ctr005_empty_hooks(self):
        ctr005_errors = self.outputs["CTR005"]
        expected_errors = [
            {"line": 137, "col": 0},  # pass
            {"line": 144, "col": 0},  # return None
            {"line": 151, "col": 0},  # return empty Result
        ]
        self.assertListEqual(ctr005_errors, expected_errors)

    def test_ctr007_parameter_definition(self):
        ctr007_errors = self.outputs["CTR007"]
        expected_errors = [
            {"line": 40, "col": 8},  # denomination literal string
            {"line": 48, "col": 8},  # nominated_account const without PARAM_
        ]
        self.assertListEqual(ctr007_errors, expected_errors)

    def test_ctr008_parameter_definition(self):
        ctr008_errors = self.outputs["CTR008"]
        expected_errors = [
            {"line": 43, "col": 8},  # First letter capitalised, second word lowercase
        ]
        self.assertListEqual(ctr008_errors, expected_errors)


class FeatureLinterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ast.parse(load_file_contents(FEATURE_FILE))
        cls.linter = ContractLinter(tree, filename="library/features/v4/dummy_v4_feature.py")
        cls.outputs = defaultdict(lambda: [])
        for line, col, msg, _ in cls.linter.run():
            cls.outputs[msg[:6]].append({"line": line, "col": col})

    def test_ctr001_datetime_now_utcnow(self):
        ctr001_errors = self.outputs["CTR001"]
        expected_errors = [{"line": 13, "col": 10}, {"line": 14, "col": 13}]
        self.assertListEqual(ctr001_errors, expected_errors)

    def test_ctr002_event_types(self):
        ctr002_errors = self.outputs["CTR002"]
        expected_errors = [{"line": 9, "col": 0}]  # supported_denoms
        self.assertListEqual(ctr002_errors, expected_errors)

    def test_ctr003_4_typehinting(self):
        ctr003_4_errors = self.outputs["CTR003"] + self.outputs["CTR004"]
        expected_errors = [
            {"line": 12, "col": 23},  # no vault typehint
            {"line": 12, "col": 30},  # no argument typehint
            {"line": 12, "col": 0},  # no return
            {"line": 18, "col": 23},  # no vault typehint
        ]
        self.assertListEqual(ctr003_4_errors, expected_errors)


class ListMetadataVisitorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ast.parse(load_file_contents(CONTRACT_FILE))
        cls.visitor = ListMetadataVisitor(tree, contract_version="3")
        cls.outputs = defaultdict(lambda: [])
        cls.visitor.visit(tree)
        for line, col, msg in cls.visitor.violations:
            cls.outputs[msg].append({"line": line, "col": col})

    def test_get_non_hook_non_helper_funcs(self):
        result = self.visitor.non_hook_non_helper_funcs
        self.assertSetEqual(result, {"extend_event_types", "_helper_function"})
        self.assertNotIn("post_parameter_change_hook", result)
        self.assertNotIn("_pre_parameter_change_hook_helper_function", result)


class GetParameterVisitorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ast.parse(load_file_contents(GET_PARAMETER_EXAMPLE_FILE))
        cls.visitor = GetParameterVisitor()
        cls.outputs = defaultdict(lambda: [])
        cls.visitor.visit(tree)
        for line, col, msg in cls.visitor.violations:
            cls.outputs[msg].append({"line": line, "col": col})

    def test_ctr006_get_parameter(self):
        ctr006_errors = self.outputs[ERRORS_CTR006]
        expected_errors = [{"line": 12, "col": 15}]  # literal string used
        self.assertListEqual(ctr006_errors, expected_errors)

    def test_ctr006b_get_parameter(self):
        ctr006b_errors = self.outputs[ERRORS_CTR006B]
        expected_errors = [{"line": 8, "col": 10}]  # kwarg not used
        self.assertListEqual(ctr006b_errors, expected_errors)


class PidVisitorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ast.parse(load_file_contents(PID_EXAMPLE_FILE))
        cls.visitor = PidVisitor()
        cls.outputs = defaultdict(lambda: [])
        cls.visitor.visit(tree)
        for line, col, msg in cls.visitor.violations:
            cls.outputs[msg].append({"line": line, "col": col})

    def test_ctr009_no_valuedatetime_in_pid(self):
        ctr009_errors = self.outputs[ERRORS_CTR009]
        expected_errors = [{"line": 8, "col": 0}]
        self.assertListEqual(ctr009_errors, expected_errors)


class EmptyHookVistorTest(unittest.TestCase):
    def test_empty_hook_visitor_raises_if_not_contract_or_supervisor(self):
        with self.assertRaises(ValueError):
            EmptyHookVisitor(contract_file_type=SmartContractFileType.FEATURE)
