"""
https://leetcode.com/problems/product-of-array-except-self
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # make 2 arrays, one to store products of elements to the left, and one for storing product of elements to the right.

        # initialize array by all 1's
        left_product_array = [1 for i in range(len(nums))]
        right_product_array = [1 for i in range(len(nums))]

        # start from the first index, because the product of the element to the left most elelemnt will always be 1
        left_product_till_now = 1
        for index, num in enumerate(nums):
            if index == 0:
                continue

            left_product_till_now = left_product_till_now * nums[index - 1]
            left_product_array[index] = left_product_till_now

        # calculate right product array now
        right_product_till_now = 1
        index = len(
            nums) - 2  # we will start fro second last elemeent, as the last element will have the same 1 as product of all right elelemts
        while index >= 0:
            right_product_till_now = right_product_till_now * nums[index + 1]
            right_product_array[index] = right_product_till_now

            index -= 1

        # at the end, multiply both arrays, and return result

        result = []

        count = 0
        while count < len(nums):
            element = left_product_array[count] * right_product_array[count]
            result.append(element)

            count += 1

        return result
