class Solution:

    def heapifyDown(self, arr, ind):
        n = len(arr)  
        largestInd = ind

        leftChildInd = 2*ind + 1
        rightChildInd = 2*ind + 2
        if leftChildInd < n and arr[leftChildInd] > arr[largestInd]:
            largestInd = leftChildInd
        if rightChildInd < n and arr[rightChildInd] > arr[largestInd]:
            largestInd = rightChildInd
        if largestInd != ind:
            arr[largestInd], arr[ind] = arr[ind], arr[largestInd]
            self.heapifyDown(arr, largestInd)
        return

        def minToMaxHeap(self, nums):
            n = len(nums) 
            for i in range(n//2 - 1, -1, -1):
                self.heapifyDown(nums, i)
            return nums

        
        # If the left child holds larger value, update the largest index
        if leftChildInd < n and arr[leftChildInd] > arr[largestInd]:
            largestInd = leftChildInd

        # If the right child holds larger value, update the largest index
        if rightChildInd < n and arr[rightChildInd] > arr[largestInd]:
            largestInd = rightChildInd

        # If the largest element index is updated
        if largestInd != ind:
            # Swap the largest element with the current index
            arr[largestInd], arr[ind] = arr[ind], arr[largestInd]

            # Recursively heapify the lower subtree
            self.heapifyDown(arr, largestInd)
        return

    def minToMaxHeap(self, nums):
        n = len(nums)
        
        # Iterate backwards on the non-leaf nodes
        for i in range(n//2 - 1, -1, -1):
            # Heapify each node downwards
            self.heapifyDown(nums, i)
        
        return nums

     
