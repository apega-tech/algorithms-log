"""
Reverse a Singly Linked List
Reverse the direction of a singly linked list in place.

Approach: iterate with three pointers (prev, current, next), relinking
as we go.
Time: O(n)   Space: O(1)
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


if __name__ == "__main__":
    # build 1 -> 2 -> 3 -> 4
    head = Node(1, Node(2, Node(3, Node(4))))
    reversed_head = reverse_list(head)
    assert to_list(reversed_head) == [4, 3, 2, 1]
    print("All tests passed.")
