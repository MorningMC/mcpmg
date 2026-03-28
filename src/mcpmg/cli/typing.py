import os
from datetime import datetime, date, time

type StrPath = str | os.PathLike[str]

type TomlElement = dict[str, TomlElement] | list[TomlElement] | str | int | float | bool | datetime | date | time