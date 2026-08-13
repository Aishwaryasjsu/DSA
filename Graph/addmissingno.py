class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        sum=n*(n+1)//2
        sumArray = 0
        for num in nums:
            sumArray=sumArray+num
        return sum-sumArray