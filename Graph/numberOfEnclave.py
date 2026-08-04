class Solution:
    def valid(self, i, j, n, m):
        
        # Return false if cell is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        
        # Return true if cell is valid
        return True

    def bfs(self,grid,ans,q,n,m):

        dirR=[-1, 0, 1, 0]
        dirC=[0, 1, 0, -1]
        while q:
            row,col=q.popleft()
            for i in range(4):
                nr=row+dirR[i]
                nc=col+dirC[i]
                if self.valid(nr,nc,n,m) and  ans[nr][nc]==False and  grid[nr][nc] == 1 :
                    q.append((nr,nc))
                    ans[nr][nc]=True


    def numberOfEnclaves(self, grid):
        n=len(grid)
        m=len(grid[0])
        q=deque()
        ans = [[False] * m for _ in range(n)] 
        for i in  range(n) :
            for j in range(m) :
                if  ((i==0 or i==n-1 ) or  (j==0 or j==m-1 )) and  grid[i][j]==1:
                    q.append((i,j))
                    ans[i][j]=True
        self.bfs(grid,ans,q,n,m)
        count=0
        for i in range(n):
            for j in range(m) :
                if grid[i][j]==1 and ans[i][j]==False:
                    count+=1
        return count



   