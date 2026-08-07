class Solution:
    #binary search log(N)
    def findMin(self, arr):
        minele=float('inf')
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[low] <= arr[mid]:
                minele=min(minele,arr[low])
                low = mid + 1
            else:
                minele= min(minele, arr[mid])
                high=mid-1
        # return maxele
        mine =float('inf')
        for i in range(len(arr)):
            if arr[i]<mine:
                mine=min(mine,arr[i])
        return mine
