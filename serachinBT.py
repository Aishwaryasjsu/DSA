class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        if root.data ==val:
            return root
        if val>root.data:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)