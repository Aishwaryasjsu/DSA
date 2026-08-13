class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        hm={}
        hm1={}

        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in hm and t[i] not in hm1:
                    hm[s[i]]=t[i]
                    hm1[t[i]]=s[i]
                elif  s[i] in hm and hm[s[i]]!=t[i] :
                    return False
                elif  t[i] in hm1 and hm1[t[i]]!=s[i]:
                    return False
            return True
