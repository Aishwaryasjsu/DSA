# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def sortList(self, head):
        dummy0=ListNode(-1)
        dummy1=ListNode(-1)
        dummy2=ListNode(-1)

        d0=dummy0
        d1=dummy1
        d2=dummy2   
        temp=head
        while(temp is not None):
            if temp.data==0:
                dummy0.next=ListNode(0)
                dummy0=dummy0.next  
            elif temp.data==1:
                dummy1.next=ListNode(1)
                dummy1=dummy1.next  
            else:
                dummy2.next=ListNode(2)
                dummy2=dummy2.next 
            temp=temp.next 
        dummy2.next=None
        dummy1.next=d2.next
        dummy0.next=d1.next
        return d0.next
                 
                 
                



      