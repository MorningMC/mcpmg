from sys import stdin

from ..core.typing import GenericStrPath


def convert_if_int(value: str) -> str | int:
	"""
	Convert a string to integer if it is a digit, or return the string as it is otherwise.

	:param value: The string to be converted.
	:return: The converted integer or the original string.
	"""

	return int(value) if value.isdigit() else value


def read_file_or_stdin(path: GenericStrPath = '-') -> str:
	"""
	Read and return the content of a file, or the stdin stream if ``path`` is a literal string ``-``.

	:param path: A path-like object, or a literal ``-``.
	:return: The content of the specified file or stdin.
	"""

	if path == '-':
		return stdin.buffer.read().decode()

	with open(path) as file:
		return file.read()