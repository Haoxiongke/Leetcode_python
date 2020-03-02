"""
Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""

class Solution(object):
    def isValid(self, s):
        """
        有效的括号
        :type s: str
        :rtype: bool
        """
        stack = []
        d = ["()", "[]", "{}"]
        for i in range(0, len(s)):
            stack.append(s[i])
            print(stack)
            if len(stack) >= 2 and stack[-2] + stack[-1] in d:
                stack.pop()
                stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid("[()]"))
