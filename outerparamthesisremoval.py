class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Your code goes here
        res=[]
        b=0
        for c in s:
            if c=="(":
                if b > 0:
                    res.append(c)
                b += 1
            else:
                b -= 1
                if b > 0:
                    res.append(c)
        return ''.join(res)
