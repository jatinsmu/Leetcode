"""
https://leetcode.com/problems/valid-anagram
"""


class Solution:
    def getMap(self, word) -> dict:
        map = {}
        wordList = list(word)
        for w in wordList:
            if w in map:
                map[w] += 1
            else:
                map[w] = 1

        return map

    # Approach 1
    # check the frequency of characters in both strings. If it matches, return True, else False
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s = self.getMap(s)
        map_t = self.getMap(t)

        for i in list(s):
            if i in map_t and map_s[i] == map_t[i]:
                continue
            else:
                return False

        return True

    # Approach -2
    # Split charcters of first string in list, then iterate through second string char by char and remove matching characters from first list. At the end, if lenght of first list is 0, then True, else False

    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) == len(t):
    #         list1 = list(s)

    #         for char in t:
    #             if char in list1:
    #                 list1.remove(char)

    #         return len(list1) == 0

    #     return False
