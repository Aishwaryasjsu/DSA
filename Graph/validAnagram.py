class Solution:    
    def anagramStrings(self, s, t):
        if len(s)!=len(t):
            return False
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')]+=1
        for c in t:
            count[ord(c)-ord('a')]-=1

        for c in count:
            if c !=0:
                return False
        return True

            