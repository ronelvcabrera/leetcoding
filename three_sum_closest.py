"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

def threeSumClosest(nums, target):
    diff = float('inf')
    nums.sort()
    for i in range(len(nums)):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - sum) < abs(diff):
                diff = target - sum
            if sum < target:
                lo += 1
            else:
                hi -= 1
        if diff == 0:
            break
    return target - diff

def threeSumClosest_mine(nums, target):
    nums.sort()
    diffs = [(idx, abs(target - num)) for idx, num in enumerate(nums)]
    diffs.sort(key=lambda differ: differ[1])
    print(diffs)
    diffs = diffs[0:3]
    print(diffs)
    diffs = [nums[set[0]] for set in diffs]
    print(diffs)
    total = sum(diffs)
    return total


print(threeSumClosest([0,2,1,-3], 1))