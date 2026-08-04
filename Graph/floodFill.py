class Solution:
    def valid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True

    def dfs(self,row,col,image,ans,newColor,startColor):
        rowdir=[0,-1,0,1]
        coldir=[-1,0,1,0]
        ans[row][col] =newColor  
        n=len(image)
        m=len(image[0])
        for i in range(4):
            nr=row+rowdir[i]
            nc=col+coldir[i]
            if self.valid(nr,nc,n,m) and image[nr][nc]==startColor and ans[nr][nc]!=newColor:
                self.dfs(nr,nc,image,ans,newColor,startColor)
                

    def floodFill(self, image, sr, sc, newColor):
        startColor=image[sr][sc]

        ans =[ row[:] for row in image]

        self.dfs(sr,sc,image,ans,newColor,startColor)

        return ans 



      