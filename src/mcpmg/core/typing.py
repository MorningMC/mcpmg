import os
from re import Pattern
from typing import Type, IO

__all__ = (
	'GenericStr',
	'Raisable',
	'OrError',
	'GenericStrPath',
	'PathOrBuffer',
	'StrPattern',
	'Rectangle',
	'UVArea',
	'JsonElement'
)

# Represent a string or a byte array. This type is used to replace typing.AnyStr.
type GenericStr = str | bytes

# Represent exceptions that can be passed to raise keyword.
type Raisable = BaseException | Type[BaseException]

# Represent an object or an exception. This type is used by raise_if_error method in utils method.
type OrError[T] = T | Raisable

# Represent anything that can be a filesystem path. The path can be a string, byte array, or an os.PathLike object.
type GenericStrPath = GenericStr | os.PathLike[str] | os.PathLike[bytes]

# Represent a filesystem path or a I/O stream buffer. This type is used by Pillow's image open/close operations.
type PathOrBuffer = GenericStrPath | IO[bytes]

# Represent a string pattern in regular expression.
type StrPattern = str | Pattern[str]

# Represent a rectangle area in an image, which its elements represents left, upper, right, and lower bound
# respectively, which ranges from 0 to the image's width/height. This type is used by crop method in Image instances.
type Rectangle = tuple[float, float, float, float]

# Represent a rectangle UV area. The texture's width and height are mapped to 0~1, allowing textures to fit, scale, or
# repeat if values exceed the range. Noticeably, Rectangle and UVArea represents different things despite having the same
# definition. Elements in Rectangle ranges from 0 to the image's width/height, while elements in UVArea ranges from 0~1.
type UVArea = tuple[float, float, float, float]

# Represent all types that can be converted to JSON elements.
type JsonElement = (dict[str, JsonElement] | list[JsonElement] | tuple[JsonElement, ...] |
                    str | int | float | bool | None)
