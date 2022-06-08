"""
Note: in most places where deleting an element from the middle of a list may have been more convenient, a swap is used.
      This is because deletes are worse case O(n) operations whereas swaps are O(1) operations.
"""
from typing import Any, Callable, List, Optional


class Stream:
    def __init__(self, streamable: List[Any]):
        self.stream = streamable

    # Intermediate methods (returns the stream)

    def distinct(self):
        found = set()

        write_idx = 0

        for i in range(len(self.stream)):
            element = self.stream[i]

            if element not in found:
                found.add(element)
                self._swap_elements(write_idx, i)
                write_idx += 1

        self._delete_last_elements(write_idx)

        return self

    def filter(self, function: Callable[[Any], bool]):
        write_idx = 0

        for i in range(len(self.stream)):
            element = self.stream[i]

            if function(element):
                self._swap_elements(write_idx, i)
                write_idx += 1

        self._delete_last_elements(write_idx)

        return self

    def map(self, function: Callable[[Any], Any]):
        for i in range(len(self.stream)):
            self.stream[i] = function(self.stream[i])

        return self

    def limit(self, max_size: int):
        stream_size = len(self.stream)

        if max_size < stream_size:
            self._delete_last_elements(stream_size - max_size)

        return self

    def skip(self, n):
        write_idx = 0

        for i in range(n, len(self.stream)):
            self._swap_elements(write_idx, i)
            write_idx += 1

        self._delete_last_elements(n)

        return self

    def sort(self):
        self.stream.sort()

        return self

    # Terminal methods

    def all(self, function: Callable[[Any], bool]) -> bool:
        for element in self.stream:
            if not function(element):
                return False

        return True

    def any(self, function: Callable[[Any], bool]) -> bool:
        for element in self.stream:
            if function(element):
                return True

        return False

    def count(self) -> int:
        return len(self.stream)

    def find_first(self, function: Callable[[Any], bool]) -> Optional[Any]:
        for element in self.stream:
            if function(element):
                return element

        return None

    def for_each(self, function: Callable[[Any], None]) -> None:
        for element in self.stream:
            function(element)

    def list(self) -> List[Any]:
        return self.stream

    def max(self) -> Optional[Any]:
        if not self.stream:
            return None

        maximum = self.stream[0]

        for element in self.stream:
            maximum = max(element, maximum)

        return maximum

    def min(self) -> Optional[Any]:
        if not self.stream:
            return None

        minimum = self.stream[0]

        for element in self.stream:
            minimum = min(element, minimum)

        return minimum

    def sum(self):
        return sum(self.stream)

    # private helper methods

    def _delete_last_elements(self, n):
        for _ in range(n):
            self.stream.pop()

    def _swap_elements(self, i, j):
        self.stream[i], self.stream[j] = self.stream[j], self.stream[i]


# Syntactic sugar to use the Stream class
def stream(streamable):
    return Stream(streamable)
