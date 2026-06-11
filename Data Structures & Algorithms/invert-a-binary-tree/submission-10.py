# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use DFS to invert 

        # base case:
        # if root doesn't exist, return
        if not root:
            return

        # swap children
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursive case:
        # run self.invertTree on left child
        self.invertTree(root.left)
        # run self.invertTree on right child
        self.invertTree(root.right)

        # return root
        return root