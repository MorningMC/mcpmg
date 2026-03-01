from typing import override

from . import *
from ..model import Model
from ..model.player import PlayerModel
from ..typing import JsonElement


class GeoJsonSerializer(Serializer[JsonElement]):

	@override
	def serialize(self, model: Model) -> JsonElement:
		...


class GeoJsonFinalSerializer(FinalSerializer[str]):

	@override
	def serialize(self, model: PlayerModel) -> str:
		...

# TODO implement GeoJsonSerializer and GeoJsonFinalSerializer here