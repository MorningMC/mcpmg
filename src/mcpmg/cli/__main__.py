import sys
import logging

from ..core import skin
from . import logger
from .parser import parse_arguments


def configure_logger(log_file: str | None, level: int | str, quiet: bool):
	"""Configures the root logger of logging module."""

	# Map level names to number codes
	logging.addLevelName(logging.NOTSET, 'notset')
	logging.addLevelName(logging.DEBUG, 'debug')
	logging.addLevelName(logging.INFO, 'info')
	logging.addLevelName(logging.WARNING, 'warning')
	logging.addLevelName(logging.ERROR, 'error')
	logging.addLevelName(logging.CRITICAL, 'critical')

	# Configure for loggers
	logging.basicConfig(filename=log_file, filemode='w', level=level)

	if not log_file and quiet:
		logging.disable()


def main():
	"""The entry function of CLI module."""

	arguments = parse_arguments()

	configure_logger(arguments.log_file, arguments.log_level, arguments.quiet)
	logger.debug(f'Parsed argument namespace: {arguments}')

	# Pillow would accept both file path and IO streams
	source = arguments.input if arguments.input else sys.stdin.buffer


if __name__ == '__main__':
	main()
