from abc import ABC

from .serialize import Serializable


class Model(ABC, Serializable):
	...