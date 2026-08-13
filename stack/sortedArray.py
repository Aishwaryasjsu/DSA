class Solution:
    def checkingSorted(self,i,n,nums):
        if i>n:
            return True
        if nums[i]>nums[i+1]:
            return False
        return self.checkingSorted(i+1,n,nums)

    def isSorted(self, nums):
        n=len(nums)-2
        return self.checkingSorted(0,n,nums)


        