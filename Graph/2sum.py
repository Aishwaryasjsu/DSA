class Solution:
    def twoSum(self, nums, target):
        hm={}
        for i  in range(len(nums)) :
            num=target-nums[i]
            if num in hm:
                return [hm[num],i]
            hm[nums[i]]=i
        return [-1,-1]

        