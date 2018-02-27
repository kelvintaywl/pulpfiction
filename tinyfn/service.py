from .exceptions import FunctionLengthExceedLimit
from .parser import Directory as DirectoryParser
from .validator import Function as FunctionValidator


def evaluate(path: str, max_length: int) -> None:
    parser = DirectoryParser(path)
    for _file in parser:
        for fn in _file:
            try:
                validate = FunctionValidator(fn, max_length)
                assert bool(validate)
            except AssertionError:
                raise FunctionLengthExceedLimit.from_validator(validate)
