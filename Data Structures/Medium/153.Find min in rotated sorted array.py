class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        minimum = float(inf)  # can ignore maybe

        while left < right:
            mid = (left + right) // 2

            minimum = min(minimum, nums[mid])  # update minumum to the min of mid element and current

            if nums[mid] > nums[right]:
                # go to the right section as mid element is greater than leftmost one
                left = mid + 1
            else:
                right = mid - 1

        return min(minimum, nums[
            left])  # take minimum of min and leftmost coz in the else condition, we move to the left section even if the mid element was equal to the rightmost element
