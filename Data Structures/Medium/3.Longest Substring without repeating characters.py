def lengthOfLongestSubstring(s: str) -> int:
    charset = set()
    left = 0
    right = 0
    longest = 0

    while right < len(s):

        while s[right] in charset:
            # char is already in set so remove char at the left pointer and bring left one forward
            # removing char at left because we wnat to shift the string to left since we want a continuous substring
            # removing left will mean we are keeping a continuos string with the element at current right index
            # although it we remove and add the same element since at this point left and right are both same elelemt, but
            # but to make left pointer of the correct index, we do this. we shift left pointer forward.
            charset.remove(s[left])
            left += 1

        charset.add(s[right])

        longest = max(longest, right - left + 1)  # right-left+1 is length of current substring

        right += 1

    return longest


print(lengthOfLongestSubstring("pwwkew"))
s = 'aaa'
s.find('a')