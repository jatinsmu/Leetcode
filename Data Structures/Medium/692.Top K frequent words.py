"""
https://leetcode.com/problems/top-k-frequent-words
"""

from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # create a map where key is the element and value is the frequency, then reverse it
        map = {}  # {i:2, love:2, leetcode:1, coding:1}
        for word in words:
            if word not in map:
                map[word] = 1
            else:
                map[word] += 1

        new_map = {}  # {2: [i, love], 1:[leetcode,coding]}

        for word, freq in map.items():
            if freq not in new_map:
                new_map[freq] = [word]
            else:
                new_map[freq].append(word)

        # now get elements from new_map from top frequencies, until we reach the k number of elements present in the keys
        frequencies = sorted(list(new_map.keys()), reverse=True)  # [2,1]
        elements_added = 0
        result = []
        counter = 0
        while elements_added < k and counter < len(frequencies):
            current_freq = frequencies[counter]
            curr_elements = new_map[current_freq]
            length_of_current_freq = len(curr_elements)
            if length_of_current_freq > 1:
                curr_elements.sort()

            if length_of_current_freq + elements_added > k:
                # means we need to pick just the ones that we want from curr_elements
                elements_to_add = curr_elements[:k - elements_added]
                result.extend(elements_to_add)
                elements_added = elements_added + len(elements_to_add)
            else:
                result.extend(curr_elements)
                elements_added = elements_added + length_of_current_freq

            counter += 1

        return result
