# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None, child=None):
#         self.val = val
#         self.next = next
#         self.child = child

class Solution:
    def merge(self,l1,l2):
        dummyNode=ListNode(-1)
        res=dummyNode
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                res.child = l1
                res=l1
                l1 = l1.child
            else:
                res.child = l2
                res=l2
                l2=l2.child
            res.next = None
        if l1:
            res.child = l1
        else:
            res.child=l2
        if dummyNode.child:
            dummyNode.child.next = None
        return dummyNode.child

    def flattenLinkedList(self, head):
        if head is None or head.next is None:
            return head 
        mergedHead = self.flattenLinkedList(head.next)
        head = self.merge(head, mergedHead)
        return head
    def printLinkedList(head):
        while head is not None:
            print(head.val, end=" ")
            head = head.child
        print()
    def printOriginalLinkedList(head, depth):
        while head is not None:
            print(head.val, end="")


        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)


        if head.next:
            print()
            for i in range(depth):
                print("| ", end="")
        
        head = head.next
