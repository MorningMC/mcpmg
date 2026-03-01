import os
from typing import IO

type AnyStr = str | bytes

type AnyStrPath = AnyStr | os.PathLike[AnyStr]
type PathOrBuffer = AnyStrPath | IO[bytes]

type Box = tuple[float, float, float, float]

type JsonElement = dict[str, JsonElement] | list[JsonElement] | tuple[JsonElement, ...] | str | int | float | bool | None