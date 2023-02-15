from struct import unpack


class ByteBuffer:

    def __init__(self, buffer: bytes) -> None:
        self._buffer = buffer

    def cut_buffer(self, length: int) -> None:
        self._buffer = self._buffer[length:]

    def pop(self) -> int:
        data = self._buffer[0]
        self.cut_buffer(1)
        return data

    def read_string(self) -> str:
        length = self.pop()
        data = self._buffer[:length].decode("utf-8")
        self.cut_buffer(length)
        return data

    def read_integer(self) -> int:
        length = 4
        data = unpack(">i", self._buffer[:length])[0]
        self.cut_buffer(length)
        return data

