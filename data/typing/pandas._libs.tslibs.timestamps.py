from typing import *


class _Timestamp:
    @classmethod
    def to_datetime64(_0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "usage.xarray: 1"

    @classmethod
    def to_pydatetime(_0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "usage.xarray: 1"


class Timestamp:
    def __init__(ts_input):
        "usage.xarray: 25"

    tz = ...
    value = ...

    def __rsub__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        ""

    def __radd__(
        self,
        _0: Union[
            (
                pandas.core.indexes.timedeltas.TimedeltaIndex,
                pandas._libs.tslibs.nattype.NaTType,
                pandas._libs.tslibs.timedeltas.Timedelta,
            )
        ],
        /,
    ):
        ""