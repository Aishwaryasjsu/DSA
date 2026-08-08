from collections import deque

class Solution:
    def topoSort(self, V, adj):
 
        ans = []
        
        # To store the ID of nodes
        inDegree = [0] * V
        
        # Calculating the ID of the given graph
        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1
        
   
        q = deque()
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
        
 
        while q:
       
            node = q.popleft()
            ans.append(node)
            
            # Traverse the neighbours
            for it in adj[node]:
                inDegree[it] -= 1
                
                if inDegree[it] == 0:
                    q.append(it)
        return ans

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        topo = self.topoSort(V, adj)
        
        if len(topo) < V:
            return True
    
        return False

