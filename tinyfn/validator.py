import math

from .models import Function


class Function:

    def __init__(self, function: Function, max_lines: int) -> None:
        self.function = function
        self.max_lines = max_lines

    def is_valid(self) -> bool:
        try:
            self.validate()
        except AssertionError:
            return False
        else:
            return True

    def validate(self) -> None:
        assert len(self.function) <= self.max_lines

    def __bool__(self) ->bool:
        return self.is_valid()
