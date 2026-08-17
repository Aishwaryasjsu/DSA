class Solution:
    def roseGarden(self, n, nums, k, m):
        mini=min(nums)
        maxi=max(nums)
        left =mini
        right=maxi
     
        if m* k>n:
            return -1
        while left<=right:
            mid=(left+right)//2
            noOfB=0
            count=0
            for n in nums:
                if n<=mid:
                    count+=1
                else:
                    noOfB+=count//k
                    count=0
            noOfB += (count // k) 
            if noOfB >=m:
                right=mid-1
            else:
                left=mid+1
        return left

     
