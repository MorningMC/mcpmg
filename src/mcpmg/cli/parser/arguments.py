import argparse
from typing import Optional, override

from ...core.typing import PathOrBuffer
from .. import logger


class ParsedArguments(argparse._AttributeHolder):
	"""
	Represent parsed command-line arguments. This class provides some property-method to simplify and abstract logics.
	"""

	def __init__(self, namespace: argparse.Namespace):
		self.namespace = namespace

	def __getattr__(self, item):
		return getattr(self.namespace, item)

	def __contains__(self, item):
		return item in self.namespace

	def __eq__(self, other):
		if isinstance(other, ParsedArguments):
			return self.namespace == other.namespace

		return False

	@override
	def _get_kwargs(self):
		return self.namespace.__dict__.items()

	@property
	def skin_output(self) -> Optional[PathOrBuffer]:
		"""
		Return the output destination of modified skin texture.

		:return: The output destination of modified skin texture. Can be a filename (string), ``os.PathLike``
		object or a file object. ``None`` represents no output.
		"""

		if self.namespace.dont_modify_skin:
			return None

		if self.namespace.skin_output:
			return self.namespace.skin_output

		logger.warning(f'Skin texture output is ignored.')
		return None

	@property
	def slim_variant_skin(self) -> Optional[bool]:
		"""
		Return the variant of the skin specified by the user.

		:return: ``true`` if the skin is a slim-armed (Alex) skin, ``false`` otherwise. ``None`` represents infer
		from skin texture.
		"""

		if self.namespace.skin_variant:
			return self.namespace.skin_variant in ('alex', 'slim')

		return None