class Solution:

    MOD = 10**9 + 7

    def modPow(self, base, exp):
      
        result = 1
      
        base %= self.MOD

        while exp > 0:
           
            if exp % 2 == 1:
                result = (result * base) % self.MOD
         
            base = (base * base) % self.MOD
          
            exp //= 2
 
        return result


    def countGoodNumbers(self, n: int) -> int:

        even_positions = (n + 1) // 2
 
        odd_positions = n // 2

        res = (self.modPow(5, even_positions) * self.modPow(4, odd_positions)) % self.MOD

        return res

