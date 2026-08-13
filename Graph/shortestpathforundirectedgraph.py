class Solution:
    def bfs(self, src, adj, dist):
        dist[src] = 0 
        q = deque()
        q.append(src) 
        while q:
            node=q.popleft()
            for adjNode in adj[node]:
                if dist[node] + 1 < dist[adjNode]:
                    dist[adjNode] = 1 + dist[node]
                    q.append(adjNode)

    def shortestPath(self, edges, N, M):
        adj = [[] for _ in range(N)]
        for edge in edges:
            u = edge[0] # first node
            v = edge[1] # second node

            adj[u].append(v)
            adj[v].append(u)
        dist = [float('inf')] * N
        self.bfs(0, adj, dist)

        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist

      