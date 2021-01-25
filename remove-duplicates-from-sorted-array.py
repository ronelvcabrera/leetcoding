"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        while (True):
            if len(nums) - 1 <= idx:
                break
            if nums[idx] == nums[idx + 1]:
                nums.pop(idx + 1)
            else:
                idx += 1
        return len(nums)
        

solution = Solution()
print('Answer = ', solution.removeDuplicates([1, 1, 2, 3, 3, 4]))