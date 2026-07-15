"""
Valid Parentheses
Determine if a string of brackets ( ) [ ] { } is validly matched/nested.

Approach: stack — push opening brackets, pop and match on closing brackets.
Time: O(n)   Space: O(n)
"""


def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


if __name__ == "__main__":
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([{}])") is True
    assert is_valid("(") is False
    print("All tests passed.")
