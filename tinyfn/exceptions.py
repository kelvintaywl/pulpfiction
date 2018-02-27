from .validator import Function as FunctionValidator


class FunctionLengthExceedLimit(BaseException):

    @classmethod
    def from_validator(cls, validator: FunctionValidator):
        msg = 'Function length ({total_length}) exceeded max line length: {max_length} at: {path}:{name}'.format(
            total_length=len(validator.function),
            max_length=validator.max_lines,
            path=validator.function.filepath,
            name=validator.function.name
        )
        return cls(msg)
