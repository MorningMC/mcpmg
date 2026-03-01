from abc import ABC, abstractmethod
from typing import override

from ..model import Model
from ..model.player import PlayerModel
from ..typing import AnyStr

__all__ = (
	'Serializer',
	'FinalSerializer'
)


class Serializer[T](ABC):
	"""Abstract base class for model serializers."""

	@abstractmethod
	def serialize(self, model: Model) -> T:
		"""
		Serialize a ``Model`` object into a specific format.

		:param model: The ``Model`` object to serialize.
		:return: The serialized model in a format-specific representation (e.g., ``JsonElement`` for JSON, ``str`` for OBJ).
		"""

		...


class FinalSerializer[T: AnyStr](Serializer[T]):
	"""Abstract base class for final player model serializers."""

	@override
	@abstractmethod
	def serialize(self, model: PlayerModel) -> T:
		"""
		Serialize a ``PlayerModel`` object into a string or byte array.

		:param model: The ``PlayerModel`` object to serialize.
		:return: The serialized player model in string or byte array.
		"""

		...