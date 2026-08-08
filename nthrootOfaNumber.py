class Solution:
   
    def helperFunc(self, mid, n, m):
        ans, base = 1, mid

        while n > 0:
            if n % 2 == 1:
                ans *= base
                if ans > m:
                    return 2  
                n -= 1
            else:
                n //= 2
                base *= base
                if base > m:
                    return 2
        
        if ans == m:
            return 1
        return 0


    def NthRoot(self, N, M):
        low, high = 1, M
        
        while low <= high:
            mid = (low + high) // 2
            midN = self.helperFunc(mid, N, M)
            
            if midN == 1:
                return mid  
            elif midN == 0:
                low = mid + 1  
            else:
                high = mid - 1 
        return -1  

