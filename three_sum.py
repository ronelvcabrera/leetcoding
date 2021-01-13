"""
Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

 [0,0,0,0]
"""

def threeSum(nums):
    nums.sort()
    answers = []
    for index, value in enumerate(nums):
        if index > 0 and value == nums[index -1]:
            continue
        left = index + 1
        right = len(nums) - 1
        while left < right:
            ans = value + nums[left] + nums[right]
            if ans < 0:
                left += 1
            elif ans > 0:
                right -= 1
            else:
                # equals to zero
                answers.append([value, nums[left], nums[right]])
                current_left = nums[left]
                left += 1
                while current_left == nums[left] and left < right:
                    left += 1
    return answers


def threeSum_slow(nums):
    # Works but takes too long.
    nums =  sorted(nums)
    answers = []
    detailed = {}
    for index, value in enumerate(nums):
        for idx, val in enumerate(nums):
            if index == idx:
                continue
            for id, num in enumerate(nums):
                if idx == id or index == id:
                    continue
                sum = value + val + num
                if sum == 0:
                    dindex_arr = sorted((str(value), str(val), str(num)))
                    dindex = ",".join(dindex_arr)
                    if dindex not in detailed:
                        answers.append(sorted([value, val, num]))
                    detailed[dindex] = sorted([value, val, num])
    return answers
print(threeSum([0,0,0,0]))