class Solution:
    def minBitsFlip(self, start, goal):
        no=start^goal
        count=0
        for i in range(32):
            count+=(no&1)
            no=no>>1
        return count
