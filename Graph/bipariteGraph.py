# linear graph is also bipartite
# any graph with even length is bipartite
from collections import deque

class Solution:

    def bfs(self, start, adj, color):
        q = deque([start])
        color[start] = 0  # Mark it with a color

   
        while q:
            node = q.popleft()

            # Traverse all its neighbors
            for it in adj[node]:
       
                if color[it] == -1:
           
                    color[it] = 1 - color[node]
                    q.append(it)
             
                elif color[it] == color[node]:
                 
                    return False
        return True  

    
    def isBipartite(self, V, edges):
        color = [-1] * V

 
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)


        for i in range(V):

            if color[i] == -1:
      
                if not self.bfs(i, adj, color):
                    return False
        return True  
