class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        n=len(s)
        wordarr=[]
        while i < n:
            while i < n  and s[i]==' ':
                i+=1
         

            if i >=n:
                break
            start=i

            while i < n  and s[i]!=' ':
                i+=1
            end=i-1
            word=s[start:end+1]
            wordarr.append(word)
        result=""
        for i in range(len(wordarr)-1,-1,-1):
            result+=wordarr[i]
            if i !=0:
                result+=' '
        return result
