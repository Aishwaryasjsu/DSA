# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

class Solution:
    def reverseDLL(self, head):
        if not head:
            return None
        temp=None
        curr=head
        while(curr):
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        if temp:
            head=temp.prev
        return head
