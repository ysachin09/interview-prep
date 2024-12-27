# Description:
# Given a string containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Example 1:
# Input: "()"
# Output: true

def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # Opening brackets
            stack.append(char)
        elif char in bracket_map.keys():  # Closing brackets
            if stack == [] or bracket_map[char] != stack.pop():
                return False
        else:
            return False  # Invalid character

    return stack == []


print(is_valid("()[]"))
