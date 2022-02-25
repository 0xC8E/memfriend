# Text constants
COMMAND_PROMPT = ">"
COMMAND_SEPARATOR = " "
NEWLINE = "\n"


# Sentinels for control flow
class Sentinel:
    pass


class NullSentinel(Sentinel):
    def __repr__(self) -> str:
        return "NULL"


class SuccessSentinel(Sentinel):
    def __repr__(self) -> str:
        return "OK"


class NoTransactionSentinel(Sentinel):
    def __repr__(self) -> str:
        return "NO TRANSACTION"


class NoResultSentinel(Sentinel):
    def __repr__(self) -> str:
        return ""


NULL_SENTINEL = NullSentinel()
SUCCESS_SENTINEL = SuccessSentinel()
NO_TRANSACTION_SENTINEL = NoTransactionSentinel()
NO_RESULT_SENTINEL = NoResultSentinel()
