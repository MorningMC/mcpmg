import os
from typing import IO

type StrOrBytesPath = str | bytes | os.PathLike[str] | os.PathLike[bytes]
type ImageAccept = StrOrBytesPath | IO[bytes]