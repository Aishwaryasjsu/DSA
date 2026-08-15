from collections import deque
class Solution:
    def bfs(self,i,adjLs,vis):
        vis[i]=True
        q=deque()
        q.append(i)
        while q:
            j=q.popleft()
            for adjNodes in adjLs[j]:
                if vis[adjNodes] != True:
                    vis[adjNodes] = True
                    q.append(adjNodes)
        

    def findNumberOfComponent(self, V, edges):
        vis=[0]*V
        count=0
        adjLs =[[] for _ in range(V)]
        for edge in edges:
            adjLs[edge[0]].append(edge[1])
            adjLs[edge[1]].append(edge[0])
        for i in range(V):
            if not vis[i]:
                count+=1
                self.bfs(i, adjLs, vis)
        return count

        

       