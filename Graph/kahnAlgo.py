class Solution:

    def dfs(self, node, adj, vis, st):
     
        vis[node] = 1
        
        # Traverse all the neighbors
        for it in adj[node]:
            
          
            if vis[it] == 0:
                self.dfs(it, adj, vis, st)
       
        st.append(node)
    
 
    def topoSort(self, V, adj):
      
        ans = []
      
        st = []
    
        vis = [0] * V
        
        # Travers graph
        for i in range(V):
            
         
            if vis[i] == 0:
                self.dfs(i, adj, vis, st)
        
      
        while st:
           
            ans.append(st.pop())
        
    
        return ans

