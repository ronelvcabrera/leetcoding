"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

def two_sum(nums, target):
    seen = []
    for key, num in enumerate(nums):
        if key == 0:
            seen.append(num)
            continue
        for idx, no in enumerate(seen):
            if nums[key] + seen[idx] == target:
                return [key, idx]
        seen.append(num)
    return None

def two_sum_2(nums, target):
    store = []
    for idx, num in enumerate(nums):
        diff = target - num
        if diff not in store:
            store.append(num)
        else:
            return [idx, store.index(diff)]
    return None

print(two_sum([2,7,11,15], 9))
print(two_sum_2([2,7,11,15], 9))