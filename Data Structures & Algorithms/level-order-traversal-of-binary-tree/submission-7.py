# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use a collections.deque() to be able to popleft()
        myDeque = collections.deque()

        levelOrderResult = []

        myDeque.append(root)

        while myDeque:
            level = []
            for i in (range(len(myDeque))):
                node = myDeque.popleft()

                if node:
                    # add node value to level
                    level.append(node.val)
                    # add left child and add right child to myDeque
                    myDeque.append(node.left)
                    myDeque.append(node.right)

            if level:
                levelOrderResult.append(level)

        return levelOrderResult
