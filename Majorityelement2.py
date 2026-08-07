class Solution:
    def majorityElementTwo(self, nums):
        ans=[]
        n=len(nums)
        for i in range(n):
            if len(ans)==0 or ans[0]!=nums[i]:
                count=0
                for j in range(n):
                    if nums[i]==nums[j]:
                        count+=1
                if count > (n // 3):
                    ans.append(nums[i])
                if len(ans) == 2:
                    break
            
        return ans
        