class Solution:    
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        elif goal in s+s:
            return True
        return False