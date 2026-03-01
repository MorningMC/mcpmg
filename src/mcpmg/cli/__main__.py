import logging
from typing import Optional

from ..core.skin import MinecraftSkin
from . import logger
from .parser import parse_arguments
from .typing import StrPath


def configure_logger(log_file: Optional[StrPath], level: int | str, quiet: bool):
	"""
	Configures the root logger of ``logging`` module.

	:param log_file: The path to the log file. ``None`` represents output logs to ``sys.stderr``.
	:param level: The lowest log level to display. Both level names and number codes are supported.
	:param quiet: Whether to supress the log output of stderr. Ignored if ``log_file`` is not ``None``, as ``sys.stderr``
	is not used for log output
	"""

	# Map level names to number codes
	logging.addLevelName(logging.DEBUG, 'debug')
	logging.addLevelName(logging.INFO, 'info')
	logging.addLevelName(logging.WARNING, 'warning')
	logging.addLevelName(logging.ERROR, 'error')
	logging.addLevelName(logging.CRITICAL, 'critical')

	# Configure for loggers
	# If filename is None, basicConfig will fail by itself and use stderr instead
	logging.basicConfig(filename=log_file, filemode='w', level=level)

	# If logs outputs to stderr and quiet is set, disables all log outputs.
	if not log_file and quiet:
		logging.disable()


def main():
	"""The entry function of CLI module."""

	arguments = parse_arguments()

	configure_logger(arguments.log_file, arguments.log_level, arguments.quiet)
	logger.debug(f'Parsed arguments: {arguments}')

	_ = arguments.skin_output

	skin = MinecraftSkin.open(arguments.input, arguments.slim_variant_skin)
	logger.info(f'skin size: {skin.size}')
	logger.info(f'Slim skin: {skin.slim_variant}')


if __name__ == '__main__':
	main()
