class Solution:
    def findMax(self, v):
        maxi = float('-inf')
        n = len(v)
        
        for i in range(n):
            maxi = max(maxi, v[i])
        return maxi

    def calculatetotal(self,nums,k):
        total=0
        for num in nums:
            total+=math.ceil(num/k)
        return total


    def minimumRateToEatBananas(self, nums, h):
        low=1
        high=self.findMax(nums)
 
        while low<=high:
            mid=(low+high)//2
            total=self.calculatetotal(nums,mid)
            if total<=h:
                high = mid - 1
            else:
                low=mid+1
        return low




       