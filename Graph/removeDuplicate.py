class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        j=1
        i=0
        while(j<=n-1):
            if nums[i]!=nums[j]:
                temp=nums[i+1]
                nums[i+1]=nums[j]
                i+=1
                j+=1
            else:
                j+=1
        return i+1 