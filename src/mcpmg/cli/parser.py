import argparse


def define_io_options(parser: argparse._ActionsContainer):
	parser.add_argument(
		'-i', '--input', type=str,
		help='The path to the Minecraft skin texture used for the generated player model. If this flag is absent, '
		     'the program will listen to stdin as the skin input.'
	)
	parser.add_argument(
		'-o', '--output', type=str,
		help='The path to the exported model file. If this flag is absent, the program will print the model output to stdout.'
	)
	parser.add_argument(
		'-O', '--output-skin', type=str,
		help='The path to the exported skin texture. If this flag is absent, the program will print a warning log unless '
		     '"--dont-modify-skin" flag is set. If "--dont-modify-skin" flag presents, this flag will be ignored.'
	)
	parser.add_argument(
		'-f', '--format', type=str, default='geo', choices=('geo', 'bbs', 'bbmodel', 'obj'),
		help='The output format of the model. Must be one of "geo" for *.geo.json, "bbs" for *.bbs.json, "bbmodel" for *.bbmodel, '
		     'or "obj" for *.obj. Defaults to "geo".'
	)


def define_log_options(parser: argparse._ActionsContainer):
	parser.add_argument(
		'-L', '--log-file', type=str,
		help='The path to the file to record logs. If this flag is absent, logs will be printed to stderr unless "--quiet" flag is set.'
	)
	parser.add_argument(
		'-l', '--log-level', default='info',
		choices=('notset', 'debug', 'info', 'warning', 'error', 'critical', 0, 10, 20, 30, 40, 50),
		help='The lowest log level to display. The number formats of log levels are also supported, where 0 represents "notset", '
		     '10 represents "debug", 20 represents "info", 30 represents "warning", etc. Defaults to "info".'
	)
	parser.add_argument(
		'-q', '--quiet', action='store_true',
		help='Supress the output of stderr. This flag is ignored if "--log" flag is set.'
	)


def define_generator_options(parser: argparse._ActionsContainer):
	parser.add_argument(
		'--dont-modify-skin', action='store_true',
		help='Do not produce a modified skin texture. This flag might disable some advanced generator features.'
	)


def parse_arguments() -> argparse.Namespace:
	"""Parses CLI arguments using argparse module."""

	parser = argparse.ArgumentParser(description='A light-weight, highly customizable Minecraft player model generator utility.')

	# Define options
	define_io_options(parser.add_argument_group('I/O options', 'Options that control input and output flow.'))
	define_log_options(parser.add_argument_group('log options', 'Options that control log output.'))
	define_generator_options(parser.add_argument_group('generator options', 'Options that passed to the generator.'))

	# Parse arguments
	return parser.parse_args()