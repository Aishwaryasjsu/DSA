from collections import deque

class Solution:
    # DelRow and delCol for neighbors
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    
    # Helper Function to check if a 
    # cell is within boundaries
    def isValid(self, i, j, n, m):
        
        # Return false if cell is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
            
        # Return true if cell is valid
        return True
    
    # Function to find number of minutes 

    def orangesRotting(self, grid):
    
        n = len(grid)
        m = len(grid[0])
        
        # Variable to store time taken
        # to get all oranges rotten
        time = 0
        
        # Variable to store 
        # total count of oranges
        total = 0
        
        # Variable to store count of 
        # oranges that are rotten
        count = 0
        
     
        q = deque()
        
      
        for i in range(n):
            for j in range(m):
            
                if grid[i][j] != 0:
                    total += 1
               
                if grid[i][j] == 2:
                    q.append((i, j))
        
   
        while q:
         
            k = len(q)
            
    
            count += k
            
            for _ in range(k):
                
              
                row, col = q.popleft()
                
                # Traversing neighbor
                for i in range(4):
                    
                  
                    nRow = row + self.delRow[i]
                    nCol = col + self.delCol[i]
                    
                 
                    if (self.isValid(nRow, nCol, n, m) 
                        and grid[nRow][nCol] == 1):
                            
                        
                        grid[nRow][nCol] = 2
                        q.append((nRow, nCol))
     
            if q:
                time += 1

        if total == count:
            return time
        
        # Otherwise return -1
        return -1


