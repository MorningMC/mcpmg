from dataclasses import dataclass
from typing import Iterable


@dataclass
class Cube:
	"""Represent a single cube within a model."""

	origin: tuple[float, float, float]
	size: tuple[float, float, float]
	uv: tuple[int, int]


@dataclass
class Model:
	"""Represent a model or part of a model."""

	pivot: tuple[float, float, float]
	cubes: Iterable[Cube]
	children: dict[str, Model]