class Solution:
    def rearrangeArray(self, nums):
        i=0 
        j=1
        n=len(nums)
        union=[0]*n
        #go through array 
        for num in nums:
            if num >=0:
                union[i]=num
                i+=2
            else:
                union[j]=num
                j+=2
        return union







                
        