# Griffin Wong
# 04/25/2020
# Leetcode


'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

EXAMPLE:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for i in nums:
            if target - i >= 0:
                list_two = [index(i) for i in nums]
                new_list.append(nums.index(i))
            else:
                continue
        return new_list