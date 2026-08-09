class Solution:
    def leaders(self, nums):
        maxEle=nums[-1]
        ans=[]
        ans.append(maxEle)
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>maxEle:
                ans.append(nums[i])
                maxEle=nums[i]
        ans.reverse()
        return ans


        