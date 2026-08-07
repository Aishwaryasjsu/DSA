
class Solution:

    def kthLargestElement(self, nums, k):
        import heapq
        pq = []
        
        for i in range(k):
            heapq.heappush(pq, nums[i])
        
        # Processing element
        for i in range(k, len(nums)):
           
            if nums[i] > pq[0]:
                heapq.heappop(pq) 

              
                heapq.heappush(pq, nums[i])
        
        return pq[0]  

