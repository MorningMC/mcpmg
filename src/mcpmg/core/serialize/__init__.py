from abc import ABC, abstractmethod
from typing import Any, Type, Optional, override

from ..model import Model
from ..model.player import PlayerModel
from ..typing import GenericStr, JsonElement
from ..utils import parse_bool_string

__all__ = (
	'Serializer',
	'FinalSerializer',
	'JsonSerializer',
	'JsonFinalSerializer'
)


class Serializer[T](ABC):
	"""Abstract base class for model serializers."""

	def __init__(self, **kwargs):
		"""
		Constructs a ``Serializer`` instance using given attributes.

		:param kwargs: The attributes assigned to the serializer.
		"""

		for key, value in kwargs.items():
			setattr(self, key, value)

	@abstractmethod
	def serialize(self, model: Model) -> T:
		"""
		Serialize a ``Model`` object into a specific format.

		:param model: The ``Model`` object to serialize.
		:return: The serialized model in a format-specific representation (e.g., ``JsonElement`` for JSON, ``str`` for OBJ).
		"""

		raise NotImplementedError


class FinalSerializer[T: GenericStr](Serializer[T], ABC):
	"""Abstract base class for final player model serializers."""

	CHILD: Type[Serializer[Any]]

	@override
	def __init__(self, **kwargs):
		"""
		Constructs a ``FinalSerializer`` instance using given attributes.

		The default action of this method is constructing and assign an instance of the child serializer class with the
		same attributes as the current final serializer instance to ``child_instance`` instance property. The child
		serializer class is defined in the ``CHILD`` class property.

		:param kwargs: The attributes assigned to the final serializer.
		"""

		super().__init__(**kwargs)

		self.child_instance = self.CHILD(**kwargs)

	@override
	@abstractmethod
	def serialize(self, model: PlayerModel) -> T:
		"""
		Serialize a ``PlayerModel`` object into a string or byte array.

		:param model: The ``PlayerModel`` object to serialize.
		:return: The serialized player model in string or byte array.
		"""

		raise NotImplementedError


class JsonSerializer(Serializer[JsonElement], ABC):
	"""Abstract base class for model serializers that serialize into JSON-based formats."""

	...


class JsonFinalSerializer(FinalSerializer[str], ABC):
	"""Abstract base class for final player model serializers that serialize into JSON-based formats."""

	CHILD: Type[JsonSerializer]

	@override
	def __init__(self, indent: Optional[str] = None, compat_separators: Optional[str] = None):
		if not indent:
			self.indent = None

		elif indent == 'tab':
			self.indent = '\t'

		elif indent.isdigit():
			self.indent = int(indent)

		else:
			raise ValueError(f'Unrecognized indent value: {indent}')

		self.separators = (',', ':') if parse_bool_string(compat_separators, True) else None

		super().__init__()
