class Solution:
    def smallestDivisor(self, nums, limit):
        low =1
        high=max(nums)
        while(low<=high):
            mid=(low+high)//2
            sum=0
            for n in nums:
                sum+=math.ceil(n/mid)
            if sum <=limit:
                high=mid-1
            else:
                low=mid+1
        return low
       