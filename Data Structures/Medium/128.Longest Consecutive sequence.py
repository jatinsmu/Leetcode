"""https://leetcode.com/problems/longest-consecutive-sequence"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_length = 0

        # check the start of sequence by seeing if there is n-1 number present in the list
        # to make things easy, lets make a set so that we remove duplicates and the search time complexity will also be O(1) for each operation
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                # means this is start of a new sequence
                current_sequence_length = 1  # initiate the length of current sequence
                next_number_in_sequence = num + 1  # to look for next sequence number in set

                while next_number_in_sequence in nums_set:
                    # loop till all the next numbers are present in the set
                    current_sequence_length += 1  # increment the current sequence length
                    next_number_in_sequence += 1  # increment to get the next number in sequence

                # when while loop terminates, that means we have exhaausted one sequence, so get max lenght
                longest_length = max(longest_length, current_sequence_length)

        return longest_length
