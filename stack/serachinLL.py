"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
        
class Solution:
    def searchKey(self, head, key):
        temp=head
        while temp is not None:
            if temp.val==key:
                return True
            temp=temp.next

        return False

