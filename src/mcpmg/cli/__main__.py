import logging
from typing import Optional

from . import logger, LOGGER_PATTERN
from .argument import parse_arguments
from mcpmg.cli.definition import load_definition, parse_definition
from .typing import StrPath


def configure_logger(log_output: Optional[StrPath], level: int | str):
	"""
	Configures the root logger of ``logging`` module.

	:param log_output: The path to the log file. ``None`` represents output logs to ``sys.stderr``.
	:param level: The lowest log level to display. Both level names and number codes are supported.
	"""

	# Map level names to number codes
	logging.addLevelName(logging.DEBUG, 'debug')
	logging.addLevelName(logging.INFO, 'info')
	logging.addLevelName(logging.WARNING, 'warning')
	logging.addLevelName(logging.ERROR, 'error')
	logging.addLevelName(logging.CRITICAL, 'critical')

	# Configure for loggers
	# If filename is None, basicConfig will fail by itself and use stderr instead
	logging.basicConfig(filename=log_output, filemode='w', level=level, format=LOGGER_PATTERN)


def main():
	"""The entry function of CLI module."""

	arguments = parse_arguments()

	configure_logger(arguments.log_output, arguments.log_level)
	logger.debug(f'Parsed arguments: {arguments}')

	definition = load_definition(arguments.input)
	logger.debug(f'Model definition: {definition}')

	tasks = parse_definition(definition)


if __name__ == '__main__':
	main()