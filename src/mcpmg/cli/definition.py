import sys
import tomllib

from ..core.task import GenerationTask
from ..core.typing import GenericStrPath
from . import logger
from .typing import TomlElement
from .utils import read_file_or_stdin


def load_definition(path: GenericStrPath) -> TomlElement:
	"""
	Load and parse the TOML model definition from the given path. The path is handled by ``read_file_or_stdin``,
	meaning that a literal ``-`` can be specified to read from stdin.

	:param path: A path-like object, or a literal string ``-`` to read from stdin.
	:return: The parsed TOML model definition as a Python ``dict`` object.
	"""

	try:
		data = read_file_or_stdin(path)
	except BaseException as error:
		logger.critical('Failed to read model definition. Check if the file exists or is accessible.', exc_info=error)
		sys.exit(1)

	try:
		return tomllib.loads(data)
	except BaseException as error:
		logger.critical('Failed to decode TOML. Check if the syntax is correct.', exc_info=error)
		sys.exit(1)


def parse_definition(definition: TomlElement) -> list[GenerationTask]:
	...