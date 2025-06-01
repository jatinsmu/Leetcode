# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base condition to check if the current node is the end nodes
        if not p and not q:
            return True  # return True because both are none

        # check if any one of them is none. This will only come if both of them weren't None
        if not p or not q or p.val != q.val:
            return False  # only one of them is None or they dont have same values

        # recursive conditions

        # do on left
        is_left_same = self.isSameTree(p.left, q.left)
        # do on right
        is_right_same = self.isSameTree(p.right, q.right)

        if is_left_same and is_right_same:
            return True
        else:
            return False
