class Sentinel:
    pass


class NullSentinel(Sentinel):
    def __repr__(self) -> str:
        return "NULL"


class SuccessSentinel(Sentinel):
    def __repr__(self) -> str:
        return "OK"


NULL_SENTINEL = NullSentinel()
SUCCESS_SENTINEL = SuccessSentinel()
