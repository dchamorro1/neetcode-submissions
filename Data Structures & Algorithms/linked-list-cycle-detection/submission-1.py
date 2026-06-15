# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes = set()

        currNode = head

        while currNode != None:
            if currNode in visitedNodes:
                return True
            
            visitedNodes.add(currNode)
            currNode = currNode.next

        return False