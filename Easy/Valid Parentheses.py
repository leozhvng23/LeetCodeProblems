"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""
from collections import deque

def isValid(self, s: str) -> bool:
    """
    # using a dictionary
    dct = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }

    stack = deque([])

    for paren in s:
        if paren in dct:
            if len(stack) > 0 and stack[-1] == dct[paren]:
                stack.pop()
            else:
                return False
        else:
            stack.append(paren)

    if len(stack) == 0:
        return True
    else:
        return False
    """

    # concised version

    stack = deque([])

    for paren in s:
        if paren == '(':
            stack.append(')')
        elif paren == '[':
            stack.append(']')
        elif paren == '{':
            stack.append('}')
        elif not stack or stack.pop() != paren:
            return False

    return not stack

