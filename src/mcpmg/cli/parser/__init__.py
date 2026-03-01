from argparse import ArgumentParser

from .definitions import *
from .arguments import ParsedArguments


def parse_arguments() -> ParsedArguments:
	"""Parses CLI arguments using ``argparse`` module."""

	parser = ArgumentParser(description='A light-weight, highly customizable Minecraft player model generator utility.')

	# Define options
	define_io_options(parser.add_argument_group('I/O options', 'Options that control input and output flow.'))
	define_log_options(parser.add_argument_group('log options', 'Options that control log output.'))
	define_generator_options(parser.add_argument_group('generator options', 'Options that passed to the generator.'))

	# Parse arguments
	return ParsedArguments(parser.parse_args())