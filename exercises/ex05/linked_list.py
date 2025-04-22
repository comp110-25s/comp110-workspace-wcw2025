from __future__ import annotations

"""File defining the node class."""

__author__: str = "730481634"


class Node:
    """Defined node class from lecture."""
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

def value_at(head: Node | None, index: int) -> int:
    """Function to determine value of node at desired index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index == 0:
            return head.value
        else:
            rest: Node | None = head.next
            if rest is None:
                raise IndexError("Index is out of bounds on the list.")
            else:
                next_value: int = value_at(rest, index - 1)
                return next_value

def max(head: Node | None) -> int:
    """Function that finds max value of a node in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    else:
        next: Node | None = head.next
        next = next
        return 5
        
        


