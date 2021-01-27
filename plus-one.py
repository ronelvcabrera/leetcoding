"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
            Improvements
        """
        for idx, num in enumerate(reversed(digits)):
            id = len(digits) - 1 - idx
            if num == 9:
                digits[id] = 0
            else:
                digits[id] = num + 1
                return digits
        digits.insert(0, 1)
        return digits
        
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
            My first try
        """
        added = 1
        newData = []
        for num in reversed(digits):
            num += 1
            print('num', num)
            if added == 0:
                break
            digits.pop()
            if num == 10:
                added = 1
                newData.insert(0, 0)
            else:
                added = 0
                newData.insert(0, num)
            print('status', digits + newData)
        if added == 1:
            newData.insert(0, 1)
        return digits + newData
        
solution = Solution()

# print("Answer = ", solution.plusOne([1,2,3]))
# print("Answer = ", solution.plusOne([1,2,3,9]))
# print("Answer = ", solution.plusOne([0]))
# print("Answer = ", solution.plusOne([0, 0]))
# print("Answer = ", solution.plusOne([9]))
# print("Answer = ", solution.plusOne([9, 9]))\
print("Answer = ", solution.plusOne([9,9,9]))