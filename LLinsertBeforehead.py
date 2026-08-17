"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def insertBeforeHead(self, head: ListNode, X: int) -> ListNode:
        # Your code goes here
        newNode=ListNode(X)
        if head is None:
            head=newNode
            return head

        head.prev=newNode
        newNode.next=head
        head=newNode
        return head

        
        

    