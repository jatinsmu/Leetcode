"""
https://leetcode.com/problems/two-sum
"""

from typing import List


class Solution:

    #  O(n2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)-1):
    #         remaining_target = target - nums[i]
    #         if remaining_target in nums[i+1:]:
    #             counter = i+1
    #             while counter <= len(nums):
    #                 if nums[counter] == remaining_target:
    #                     return [i,counter]
    #                 counter += 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_traversed = {}  # {number: index}

        # loop over numbers and their indices
        for index, num in enumerate(nums):
            remaining_target = target - num
            # Check if we have already traversed remaining_target before
            if remaining_target in numbers_traversed:
                # return current index and the index of remaining_target from the map
                return [index, numbers_traversed[remaining_target]]

            numbers_traversed[num] = index
