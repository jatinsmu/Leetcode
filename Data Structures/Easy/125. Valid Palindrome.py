import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use 2 pointers, 1 from start and 1 from the end.
        s = re.sub(r'\W+', '', s).lower().replace('_', '')

        p1 = 0
        p2 = len(s) - 1
        if len(s) == 0 or len(s) == 1:
            return True

        while s[p1] == s[p2] and p1 < p2:
            p1 += 1
            p2 -= 1

        # check if both the pointers are at same location
        if p1 >= p2:
            return True
        else:
            return False
