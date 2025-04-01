"""
https://leetcode.com/problems/contains-duplicate/
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a map and if any counter is greater than 1, then return true.

        if len(nums) == 1:
            return False

        map = {}

        for num in nums:
            if num in map:
                return True
            else:
                map[num] = 1

        # worst case
        return False
