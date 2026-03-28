from dataclasses import dataclass
from collections.abc import Iterable

from ..typing import UVArea


type UV = PerFaceUV | BoxUV


@dataclass
class PerFaceUV:
	"""Represent a per-face UV map."""

	north: UVArea
	east: UVArea
	south: UVArea
	west: UVArea
	up: UVArea
	down: UVArea


@dataclass
class BoxUV:
	"""Represent a box UV map."""

	uv: UVArea

	@property
	def north(self):
		...


@dataclass
class Cube:
	"""Represent a single cube within a model."""

	origin: tuple[float, float, float]
	size: tuple[float, float, float]
	uv: UVArea


@dataclass
class Model:
	"""Represent a model or part of a model."""

	pivot: tuple[float, float, float]
	cubes: Iterable[Cube]
	children: dict[str, Model]