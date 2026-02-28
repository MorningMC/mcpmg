from PIL import Image
from PIL.PngImagePlugin import PngImageFile

from .typing import ImageAccept


class MinecraftSkin(PngImageFile):
	"""Represents a Minecraft skin image."""

	ACCEPTED_SIZES = ((64, 32), (64, 64), (128, 128), (256, 256))

	def __init__(self, fp: ImageAccept, filename: str | bytes | None = None):
		"""
		The constructor of :py:class:`MinecraftSkin`. This method will call the parent constructor and check if the
		image size is one of 64*32, 64*64, 128*128, 256*256.
		"""

		super().__init__(fp, filename)

		if self.size not in self.ACCEPTED_SIZES:
			raise ValueError(f'Invalid skin size: {self.size}')


	@staticmethod
	def open(fp: ImageAccept, formats: list[str] | tuple[str, ...] | None = None) -> MinecraftSkin:
		return Image.open(fp, 'r', formats)


if __name__ == '__main__':
	...