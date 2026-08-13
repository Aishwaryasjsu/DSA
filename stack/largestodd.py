class Solution:  
    def largeOddNum(self, s: str) -> str:
        l=len(s)-1
        odd=-1

        #your code goes here
        for i in range(l,-1,-1):
            if (int(s[i])%2)!=0:
                odd=i
                break
        j=0
        while j<=odd and s[j]=='0':
                j+=1

        return s[j:odd+1]
            



            










        