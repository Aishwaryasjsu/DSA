# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root):
        #your code goes here
        st = []
        node = root
        preorder = []
        if node is None:
            return preorder
        st.append(node)
        while st:
            node=st.pop()
            preorder.append(node.data)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return preorder
