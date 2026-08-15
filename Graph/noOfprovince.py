from collections import deque

class Solution:
    def bfs(self,i,adjL,v):
        v[i]=1
        q=deque()
        q.append(i)
        while q:
            i=q.popleft()
            for n in adjL[i]:
                if v[n]!=1:
                    v[n]=1
                    q.append(n)

    def numProvinces(self, adj):
        V=len(adj)
        v=[0]*V
        adjL=[[] for _ in range (V)]
        for i in range (V):
            for j in range(V):
                if  adj[i][j]==1 and i!=j:
                    adjL[i].append(j)
        count=0
        for i in range (V):
            if not v[i]:
                v[i]=1
                count+=1
                self.bfs(i, adjL, v)
        return count
            

        