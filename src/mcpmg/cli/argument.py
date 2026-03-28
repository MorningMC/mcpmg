from os import devnull
from argparse import ArgumentParser, Namespace
from pathlib import Path

from .utils import convert_if_int


def parse_arguments() -> Namespace:
	"""Parses CLI arguments using ``argparse`` module."""

	parser = ArgumentParser(description='A light-weight, highly customizable Minecraft player model generator utility.')

	# Model definition file
	parser.add_argument(
		'input', nargs='?', default='-',
		help='The path to the model definition file, or "-" to read from stdin. Defaults to read from stdin.'
	)

	# Logging options
	log_output = parser.add_mutually_exclusive_group()
	log_output.add_argument(
		'-q', '--quiet', action='store_const', const=Path(devnull), dest='log_output',
		help='Redirects the log output to null device. This flag contradicts with "--log-output" flag.'
	)
	log_output.add_argument(
		'-L', '--log-output', type=Path,
		help='The path to the file to record logs. If this flag is absent, logs will be printed to stderr unless '
		     '"--quiet" flag is set.'
	)

	parser.add_argument(
		'-l', '--log-level', default='info', type=convert_if_int,
		choices=('debug', 'info', 'warning', 'error', 'critical', 10, 20, 30, 40, 50),
		help='The lowest log level to display. The number formats of log levels are also supported, where 0 represents '
		     '"notset", 10 represents "debug", 20 represents "info", 30 represents "warning", etc. Defaults to "info".'
	)

	return parser.parse_args()