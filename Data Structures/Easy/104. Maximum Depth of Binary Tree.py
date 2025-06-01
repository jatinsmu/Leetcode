# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root:
            current_level = 1

            total_levels_in_left = self.maxDepth(root.left)
            total_levels_in_right = self.maxDepth(root.right)

            # return value for current level of recursion

            return current_level + max(total_levels_in_left,
                                       total_levels_in_right)  # adding current_level since current level is also considered in total depth of tree


        else:
            return 0
