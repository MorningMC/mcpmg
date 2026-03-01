from typing import Optional
from PIL import Image
from PIL.ImageFile import ImageFile

from .typing import PathOrBuffer, Box
from .utils import expect_one_of


class MinecraftSkin:
	"""Represent a Minecraft skin texture. This class is a wrapper class of ``PIL.ImageFile`` class."""

	ACCEPTED_FORMATS = ('PNG',)
	ACCEPTED_SIZES = ((64, 32), (64, 64), (128, 128))
	TRANSPARENT_THRESHOLD = 0

	def __init__(self, image: ImageFile, slim_variant: Optional[bool] = None):
		"""
		Constructs a ``MinecraftSkin`` object.

		:param image: The texture of the skin.
		:param slim_variant: Manually specify the variant of the skin. ``None`` represents infer from skin texture.
		:except ValueError: If the image format is not in ``ACCEPTED_FORMATS``, or if the image size is not in ``ACCEPTED_SIZES``.
		"""

		self.image = image
		self._slim_variant = slim_variant

		# Check if the format and size are valid.
		expect_one_of(self.image.format, self.ACCEPTED_FORMATS)
		expect_one_of(self.size, self.ACCEPTED_SIZES)

	@property
	def size(self) -> tuple[int, int]:
		"""
		Return the resolution of the image.

		:return: The resolution of the image.
		"""

		return self.image.size

	@property
	def slim_variant(self) -> bool:
		"""
		Infer the variant (arm width) of the skin texture. This is determined by checking the transparency of a pixel on
		the arm texture.
		This is a lazy-loading property-method, that once the method is executed, it will store its result and directly
		return the cached result the next time. This property can also be specified when constructing the instance.

		:return: ``true`` if the skin is a slim-armed (Alex) skin, ``false`` otherwise.
		"""
		# If the variant has already been inferred, use the cached value.
		if self._slim_variant is not None:
			return self._slim_variant

		# Legacy skins (64x32) do not support slim arms.
		if self.size[1] <= 32:
			self._slim_variant = False
			return self._slim_variant

		# For modern skins, the model is determined by the transparency of a specific pixel.
		# The image must have an alpha channel to be a slim skin.
		if self.image.mode != 'RGBA':
			self._slim_variant = False
			return self._slim_variant

		# The check location is proportional to the skin size.
		# For a 64x64 skin, the pixel is at (54, 20).
		scale = self.size[0] / 64
		check_x = int(54 * scale)
		check_y = int(20 * scale)

		alpha = self.image.getpixel((check_x, check_y))[3]
		self._slim_variant = alpha <= self.TRANSPARENT_THRESHOLD
		return self._slim_variant

	def crop(self, box: Optional[Box]):
		"""
        Returns a rectangular region from this skin image. The ``box`` parameter is a tuple defining the left, upper,
        right, and lower pixel coordinate. This method is a wrapper of ``self.image.crop(box)``.

        :param box: The crop rectangle, as a (left, upper, right, lower)-tuple.
        :returns: An ``PIL.Image.Image`` object.
        """

		return self.image.crop(box)

	@classmethod
	def open(cls, fp: PathOrBuffer, slim_variant: Optional[bool] = None) -> MinecraftSkin:
		"""
		Open a Minecraft skin texture from a filepath or a file object.

		:param fp: A filename (string), ``os.PathLike`` object or a file object. The file object must implement ``file.read``,
		``file.seek``, and ``file.tell`` methods, and be opened in binary mode. The file object will also seek to zero
		before reading.
		:param slim_variant: Manually specify the variant of the skin. ``None`` represents infer from skin texture.
		:return: A ``MinecraftSkin`` object.
		"""

		return cls(Image.open(fp, 'r', cls.ACCEPTED_FORMATS), slim_variant)