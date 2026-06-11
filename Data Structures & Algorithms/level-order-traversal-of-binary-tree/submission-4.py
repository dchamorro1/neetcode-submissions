from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS

        # put node in deque
        myDeque = deque()

        # declare levelTraversalResult list
        levelTraversalResult = []
        myDeque.append(root)

        while myDeque:
            # make an empty list for the level
            level = []
            # for each item in deque
            for i in range(len(myDeque)):
                # add it to level list, popLeft from dequeue
                currentNode = myDeque.popleft()

                if currentNode:
                    level.append(currentNode.val)
                    # add both children to dequeue if they exist
                    myDeque.append(currentNode.left)
                    myDeque.append(currentNode.right)

            if level:
                levelTraversalResult.append(level)


        return levelTraversalResult     

        