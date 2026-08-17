class Solution:  
    def longestCommonPrefix(self, strs):
        res=""
        if len(strs)==0:
            return ""
        strs.sort()
        print(strs)
        first=strs[0]
        last=strs[-1]
        ans=[]
        for i in range(min(len(first),len(last))):
            for j in range(len(strs)):
                if strs[j][i]!=first[i]:
                    return res
             
            res+=first[i]
        return res
            
