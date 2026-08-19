class Solution:
    def isHeap(self, nums):
        n = len(nums)
        for i in range(n//2 - 1, -1, -1):
            leftChildInd = 2*i + 1
            rightChildInd = 2*i + 2

            if leftChildInd < n and nums[leftChildInd] < nums[i]:
                return False
            if rightChildInd < n and nums[rightChildInd] < nums[i]:
                return False
        return True