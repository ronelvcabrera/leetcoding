"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest = nums[0]
        currentHighest = nums[0]
        for idx, num in enumerate(nums):
            if idx == 0: continue
            currentHighest = max(num, num + currentHighest)
            if currentHighest > highest:
                highest = currentHighest
        return highest

solution = Solution()
print('Answer = ', solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))