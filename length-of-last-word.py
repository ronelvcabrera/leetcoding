"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.strip(" ").split(" ")
        print(arr)
        return len(arr[0])

solution = Solution()

print('Answer = ', solution.lengthOfLastWord("a "))