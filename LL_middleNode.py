 # Definition for Singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    slow=head
    fast=head
    while(fast is not None and fast.next is not None):
        slow=slow.next
        fast=fast.next.next
    #return slow
class Solution:
    def middleOfLinkedList(self, head):
        if head is not None:
            temp=head
        while(temp is not None and temp.next is None):
            count+=1
            temp=temp.next
        middle=count//2+1
        mn=head
        for i in range(1,middle):
            mn=mn.next
        return mn

        

