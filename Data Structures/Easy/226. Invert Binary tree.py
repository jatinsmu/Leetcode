# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def swap(node):
            node.left, node.right = node.right, node.left
            return node

        q = []

        if root:
            q.append(root)

            while len(q) > 0:
                curr_node = q.pop(0)

                node_after_swap = swap(curr_node)

                if curr_node and node_after_swap and curr_node.left:
                    q.append(node_after_swap.left)
                if curr_node and node_after_swap and curr_node.right:
                    q.append(node_after_swap.right)

        return root
