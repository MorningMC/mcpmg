from re import compile, fullmatch
from typing import Any, Optional
from collections.abc import Iterable

from .typing import OrError, StrPattern


def expect_one_of(obj, iterable: Iterable):
	"""
	Check if ``obj`` is in ``iterable``. If the condition is not met, raise a ``ValueError``.

	:param obj: The object to be examined.
	:param iterable: The ``Iterable`` object that might or might not contain ``obj``.
	:raise ValueError: If ``obj`` is not in ``iterable``.
	"""

	if obj not in iterable:
		raise ValueError(f'Expect one of {iterable}, get {obj}')


def raise_if_error(value: OrError[Any]) -> Any:
	"""
	Raise ``value`` if value is a raisable exception, or return ``value`` as it is otherwise.

	:param value: The exception to raise or the object to return.
	:return: The ``value`` itself if it is not an exception.
	"""

	if isinstance(value, BaseException):
		raise value

	return value


def parse_bool_string(value: Optional[str],
                      empty_default: OrError[bool] = False,
                      mismatch_default: OrError[bool] = ValueError(f'The value matches neither true nor false pattern'),
                      true_pattern: StrPattern = compile(r'y(es)?|t(rue)?'),
                      false_pattern: StrPattern = compile(r'no?|f(alse)?')) -> bool:
	"""
	Parse a string to a boolean value.

	:param value:
	:param true_pattern:
	:param false_pattern:
	:param empty_default:
	:param mismatch_default:
	:return:
	"""

	if not value:
		return raise_if_error(empty_default)

	value = value.lower()

	if fullmatch(true_pattern, value):
		return True

	if fullmatch(false_pattern, value):
		return False

	return raise_if_error(mismatch_default)
