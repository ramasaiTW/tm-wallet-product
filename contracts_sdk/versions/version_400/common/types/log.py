import sys
from functools import lru_cache
from .....utils import symbols
from .....utils import types_utils


class Logger:
    _instance = None

    def __init__(self):
        raise Exception("Logger is a singleton. Use instance() instead.")

    def debug(self, message: str):
        sys.stderr.write(f"{message}\n")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    @classmethod
    @lru_cache()
    def _spec(cls, language_code=symbols.Languages.ENGLISH):
        if language_code != symbols.Languages.ENGLISH:
            raise ValueError("Language not supported")
        spec = types_utils.ClassSpec(
            name="Logger",
            docstring="""
            Logger is a singleton that can be used to add debug logging.
            Note that the Logger output is not yet exposed in Contract Simulation or real Vault
            execution. However, you can use it when unit testing Smart or Supervisor Contracts
            and Contract Modules.
            """,
            public_methods=[
                types_utils.MethodSpec(
                    name="debug",
                    docstring="Logs a message at debug level",
                    args=[
                        types_utils.ValueSpec(
                            name="message",
                            type="str",
                            docstring="The message to log",
                        ),
                    ],
                    examples=[
                        types_utils.Example(
                            title="A simple example",
                            code="""
                            from contracts_api import Logger

                            logger = Logger.instance()

                            def scheduled_event_hook(vault, hook_arguments):
                                logger.debug("Hello, world!")
                            """,
                        )
                    ],
                ),
                types_utils.MethodSpec(
                    name="instance",
                    docstring="A class method to access the singleton Logger instance.",
                    examples=[
                        types_utils.Example(
                            title="A simple example",
                            code="""
                            from contracts_api import Logger

                            logger = Logger.instance()

                            def post_posting_hook(vault, hook_arguments):
                                logger.debug("This prints logs when `post_posting_hook` is run!")
                            """,
                        )
                    ],
                ),
            ],
        )
        return spec
