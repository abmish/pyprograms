"""
url: https://leetcode.com/problems/two-sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def two_sum1(self, nums, target):  # First submission on LeetCode: run time 2046 ms
        for num in nums:
            other = target - num
            x = nums.index(num)
            if other in nums[x + 1:]:
                y = x + nums[x + 1:].index(other) + 1
                return [x, y]

    def two_sum2(self, nums, target):  # Second submission on LeetCode: run time 60 ms
        dict_map = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in dict_map.keys():
                return [dict_map[complement], index]
            dict_map[nums[index]] = index

    def two_sum3(self, nums, target):  # Third submission on LeetCode: run time 59 ms
        dict_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in dict_map.keys():
                return [dict_map[complement], index]
            dict_map[num] = index

    def two_sum4(self, nums, target):  # Fourth submission on LeetCode: run time 40 ms
        if len(nums) <= 1:
            return False;
        a_dict = {};
        for idx, num in enumerate(nums):
            complement = target - num;
            if complement in a_dict.keys():
                return [a_dict[complement], idx];
            a_dict[num] = idx;

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.two_sum4(self, nums, target)  # calling the best ONE :)
