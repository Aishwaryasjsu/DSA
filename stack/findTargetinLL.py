'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
'''



class Solution:
    def findPairsWithGivenSum(self, head, target):
        if head is None or not head.next :
            return []
        tail=head
        while tail.next:
            tail=tail.next
        left=head
        right=tail
        res=[]
        while(left and right and left !=right and  left.prev!=right ):
            total=left.val+right.val
            if total==target:
                res.append([left.val,right.val])
                left=left.next
                right=right.prev
            elif total>target:
                right=right.prev
            else:
                left=left.next
        return res



        tail=head
        