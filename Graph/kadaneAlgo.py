class Solution:
    def maxSubArray(self, nums):
        maxSum=float('-inf')
        prefixSum=0
        for num in nums:
            prefixSum+=num
            if prefixSum>maxSum:
                maxSum=prefixSum
            if prefixSum<0:
                prefixSum=0
        return  maxSum
        