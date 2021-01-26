"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
"""
from typing import List
import sys

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
            nums.append(target)
            nums = sorted(nums)
            return(nums.index(target))
        """
        if target not in nums:
            j = 0
            if nums[0] > target: return 0
            for i, num in enumerate(nums):
                j += 1
                if j == len(nums): break
                if num < target and target < nums[j]:
                    return j 
            return len(nums)
        else:
            return nums.index(target)

solution = Solution()
print('Answer = ', solution.searchInsert([2,3,5,6], int(sys.argv[1])))