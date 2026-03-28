from . import Model, Cube


class PlayerModel(Model):
	"""Represents a Minecraft player model, composed of various model parts."""

	def __init__(self, is_slim: bool):
		self.is_slim = is_slim
		texture_width = 64
		texture_height = 64

		# The root model has no geometry itself, it's just a container for the parts.
		super().__init__(
			pivot=(0, 0, 0),
			cubes=[],
			children=self._create_parts()
		)

	def _create_parts(self) -> dict[str, Model]:
		"""Factory method to generate the model parts."""
		head = Model(
			pivot=(0, 24, 0),
			cubes=[Cube(origin=(-4, 24, -4), size=(8, 8, 8), uv=(0, 0))],
			children={}
		)
		body = Model(
			pivot=(0, 24, 0),
			cubes=[Cube(origin=(-4, 12, -2), size=(8, 12, 4), uv=(16, 16))],
			children={}
		)
		right_leg = Model(
			pivot=(-1.9, 12, 0),
			cubes=[Cube(origin=(-3.9, 0, -2), size=(4, 12, 4), uv=(0, 16))],
			children={}
		)
		left_leg = Model(
			pivot=(1.9, 12, 0),
			cubes=[Cube(origin=(0.1, 0, -2), size=(4, 12, 4), uv=(16, 48))],
			children={}
		)

		if self.is_slim:
			right_arm = Model(
				pivot=(-5, 22, 0),
				cubes=[Cube(origin=(-7, 12, -2), size=(3, 12, 4), uv=(40, 16))],
				children={}
			)
			left_arm = Model(
				pivot=(5, 22, 0),
				cubes=[Cube(origin=(4, 12, -2), size=(3, 12, 4), uv=(32, 48))],
				children={}
			)
		else:
			right_arm = Model(
				pivot=(-5, 22, 0),
				cubes=[Cube(origin=(-8, 12, -2), size=(4, 12, 4), uv=(40, 16))],
				children={}
			)
			left_arm = Model(
				pivot=(5, 22, 0),
				cubes=[Cube(origin=(4, 12, -2), size=(4, 12, 4), uv=(32, 48))],
				children={}
			)

		return {
			"head": head,
			"body": body,
			"rightArm": right_arm,
			"leftArm": left_arm,
			"rightLeg": right_leg,
			"leftLeg": left_leg
		}
