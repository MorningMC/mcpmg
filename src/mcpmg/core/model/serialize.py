from abc import ABC, abstractmethod


class Serializable(ABC):
	"""The base class for all serializable objects."""

	@abstractmethod
	def serialize[T](self, serializer: Serializer[T]) -> T:
		...


class Serializer[T](ABC):
	pass


class GeoJsonSerializer(Serializer[str]):
	pass


class BbsJsonSerializer(Serializer[str]):
	pass


class BlockbenchSerializer(Serializer[str]):
	pass


class ObjSerializer(Serializer[str]):
	pass