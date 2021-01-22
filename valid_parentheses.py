"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    data = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    def isValid(self, s: str) -> bool:
        opens = []
        for chr in s:
            if chr in self.data:
                opens.append(chr)
            else:
                 if len(opens) == 0 or self.data[opens.pop()] != chr: return False
        return len(opens) == 0


sol = Solution()
print(sol.isValid("{()[]"))