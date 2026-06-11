# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        myDeque = collections.deque()

        completeLevelOrderTraversal = []

        myDeque.append(root)

        while myDeque:
            level = []
            for i in range(len(myDeque)):
                node = myDeque.popleft()

                if node:
                    level.append(node.val)
                    myDeque.append(node.left)
                    myDeque.append(node.right)

            if level:
                completeLevelOrderTraversal.append(level)

        return completeLevelOrderTraversal