import json
from typing import Optional, override

from . import JsonSerializer, JsonFinalSerializer
from ..model import Model, Cube
from ..model.player import PlayerModel
from ..typing import JsonElement


class GeoJsonSerializer(JsonSerializer):
	"""Serializes a Model into a list of JSON-compatible bone dictionaries."""

	@override
	def serialize(self, model: Model) -> JsonElement:
		bones = []
		for name, child in model.children.items():
			bone = {
				"name": name,
				"pivot": list(child.pivot),
				"cubes": [self._cube_to_dict(c) for c in child.cubes]
			}
			# Recursively serialize children, though our current model is flat
			if child.children:
				# This part of the format is less well-defined, assuming nested bones are not standard
				# For now, we'll just add them to the list, but this might need adjustment
				# for more complex, hierarchical models.
				bones.extend(self.serialize(child))
			bones.append(bone)
		return bones

	def _cube_to_dict(self, cube: Cube) -> dict:
		return {
			"origin": list(cube.origin),
			"size": list(cube.size),
			"uv": list(cube.uv)
		}


class GeoJsonFinalSerializer(JsonFinalSerializer):
	"""Serializes a PlayerModel to a final .geo.json string."""

	CHILD = GeoJsonSerializer

	@override
	def __init__(self, indent: str | None = None, compat_separators: Optional[str] = None):
		super().__init__(indent, compat_separators)

	@override
	def serialize(self, model: PlayerModel) -> str:
		"""
		Converts the PlayerModel into a complete .geo.json formatted string.
		"""
		bones = self.child_instance.serialize(model)

		geometry = {
			"format_version": "1.12.0",
			"minecraft:geometry": [
				{
					"description": {
						"identifier": f"geometry.player.{'alex' if model.is_slim else 'steve'}",
						"texture_width": 64, # Assuming default texture size
						"texture_height": 64
					},
					"bones": bones
				}
			]
		}
		return json.dumps(geometry, indent=self.indent, separators=self.separators)
