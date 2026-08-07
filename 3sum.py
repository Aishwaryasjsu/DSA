class Solution:
    def threeSum(self, nums: list) -> list[list]:
        n=len(nums)
        triplet_set = set()
        for i in range(n):
            hashset=set()
            for j in range(i+1,n):
                third=-(nums[i]+nums[j])
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    triplet_set.add(tuple(temp))
                hashset.add(nums[j])
        ans = [list(triplet) for triplet in triplet_set]
        return ans


        