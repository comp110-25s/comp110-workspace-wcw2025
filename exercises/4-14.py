from __future__ import annotations

class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"

def recursive_range(start: int, end: int):
    """Create a linked list with values from start to end (exclusive)."""
    if start < end:
        val: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(val, rest)
    elif start == end:
        return None
    else:
        raise Exception("Start shouldn't be greater than end!")