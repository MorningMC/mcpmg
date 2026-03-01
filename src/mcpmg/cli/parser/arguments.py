import argparse
from sys import stdin, stdout
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
	def input(self) -> PathOrBuffer:
		"""
		Return the input source of player skin texture used to generate model.

		:return: The input source of player skin texture. Can be a filename (string), ``os.PathLike``
		object or a file object.
		"""

		return self.namespace.input if self.namespace.input else stdin.buffer

	@property
	def model_output(self) -> PathOrBuffer:
		"""
		Return the output destination of generated player model.

		:return: The output destination of generated player model. Can be a filename (string), ``os.PathLike``
		object or a file object.
		"""

		return self.namespace.output if self.namespace.output else stdout.buffer

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