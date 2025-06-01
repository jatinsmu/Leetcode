class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            elif nums[mid] >= nums[l]:
                # means normal increasing order as of now
                if target > nums[mid] or target < nums[l]:
                    # means array is rotated, so choose right section to search further
                    l = mid + 1
                else:
                    # means array is not rotated, chosse left section
                    r = mid - 1

            else:
                # means it is not normal increasing order from left to mid, means array is rotated within limits of left and mid element
                if target < nums[mid] or target > nums[r]:
                    # choose left section
                    r = mid - 1
                else:
                    # choose right section
                    l = mid + 1

        # since we choose left if mid is greater or equal to left, see if target is leftmost element
        return l if target == nums[l] else -1
