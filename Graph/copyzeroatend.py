class Solution:
    def moveZeroes(self, nums):
    
        t=0
        s=0
        while (t <len(nums)):
            if nums[t]!=0:
                temp=nums[s]
                nums[s]=nums[t]
                nums[t]=temp
                s+=1
                t+=1
            else:
                t+=1
        return nums
        