"""
https://leetcode.com/problems/top-k-frequent-elements/
"""

from heapq import heappop, heappush, heapify
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        heap = []
        heapify(heap)

        # add elements to heap
        for key, occurrences in map.items():
            value = (-1 * occurrences, key)  # heap will be sorted by the occurences, and the element will be 'key'
            heappush(heap, value)

        # now get top K elements
        result = []
        counter = 0
        while counter < k:
            occurences, element = heappop(heap)
            result.append(element)
            counter += 1

        return result
