

class File:

    def __init__(self, path: str) -> None:
        self.path = path


class Function:

    def __init__(self, filepath: str, name: str, start: int, end: int) -> None:
        self.filepath = filepath
        self.name = name
        self.start = start
        self.end = end
        assert self.end >= self.start

    def __len__(self) -> int:
        return (self.end - self.start) + 1
