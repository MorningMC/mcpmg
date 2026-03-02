import argparse
from sys import stdin, stdout
from os import devnull
from pathlib import Path

from ..utils import *


__all__ = (
	'define_io_options',
	'define_log_options',
	'define_generator_options'
)


def define_io_options(parser: argparse._ActionsContainer):
	parser.add_argument(
		'-i', '--input', default=stdin.buffer, type=Path,
		help='The path to the Minecraft skin texture used for the generated player model. If this flag is absent, '
		     'the program will listen to stdin as the skin input.'
	)
	parser.add_argument(
		'-o', '--output', default=stdout.buffer, type=Path,
		help='The path to the exported model file. If this flag is absent, the program will print the model output to stdout.'
	)
	parser.add_argument(
		'-O', '--skin-output', type=Path,
		help='The path to the exported skin texture. If this flag is absent, the program will print a warning log unless '
		     '"--dont-modify-skin" flag is set. If "--dont-modify-skin" flag presents, this flag will be ignored.'
	)


def define_log_options(parser: argparse._ActionsContainer):
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


def define_generator_options(parser: argparse._ActionsContainer):
	parser.add_argument(
		'-f', '--format', default='geo', choices=('geo', 'bbs', 'bbmodel', 'obj'),
		help='The output format of the exported player model. Must be one of "geo" for GeoJSON geometry, "bbs" for '
		     'McHorse BBS model, "bbmodel" for Blockbench Model, or "obj" for Wavefront Object Format. Defaults to "geo".'
	)
	parser.add_argument(
		'-F', '--format-options', default={}, type=parse_option_set,
		help='Options passed to serializers separated by commas. For example: "key1=value1,key2=value2"'
	)
	parser.add_argument(
		'--dont-modify-skin', action='store_true',
		help='Do not produce a modified skin texture. This flag might disable some advanced generator features.'
	)
	parser.add_argument(
		'--skin-variant', choices=('steve', 'wide', 'alex', 'slim'),
		help='Manually specify the variant of the skin. "steve" and "wide" refers to wide-armed variant, while "alex" and '
		     '"slim" refers to slim-armed variant. If this flag is absent, the variant will be inferred from the skin texture.'
	)
	parser.add_argument(
		'--arm-offset', type=int, default=0,
		help='The offset of arm model in pixels. Greater value will make arms appear lower.'
	)