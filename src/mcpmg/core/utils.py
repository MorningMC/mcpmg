from typing import Iterable


def expect_one_of(obj, iterable: Iterable[...]):
	"""
	Check if ``obj`` is in ``iterable``. If the condition is not met, raise a ``ValueError``.

	:param obj: The object to be examined.
	:param iterable: The ``Iterable`` object that might or might not contain ``obj``.
	:raise ValueError: If ``obj`` is not in ``iterable``.
	"""

	if obj not in iterable:
		raise ValueError(f'Invalid skin size: expect one of {iterable}, get {obj}')