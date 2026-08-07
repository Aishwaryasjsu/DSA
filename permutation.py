class Solution:

    def nextPermutation(self, nums):
        n = len(nums)  


        ind = -1

    
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break

        ''' If no such index exists, array is in descending order
            So, reverse it to get the smallest permutation '''
        if ind == -1:
            nums.reverse()
            return

       
        for i in range(n-1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]  
                break

        # Reverse 
        nums[ind+1:] = reversed(nums[ind+1:])
        return

