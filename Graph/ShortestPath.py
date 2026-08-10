import heapq

class Solution:
    def shortestPath(self, n, m, edges):

        adj = [[] for _ in range(n + 1)]

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        dist = [float('inf')] * (n + 1)
        parent = list(range(n + 1))

        dist[1] = 0

        pq = [(0, 1)]

        while pq:
            dis, node = heapq.heappop(pq)

            # if dis > dist[node]:
            #     continue

            for adjNode, edgeWt in adj[node]:

                newDist = dis + edgeWt

                if newDist < dist[adjNode]:
                    dist[adjNode] = newDist
                    parent[adjNode] = node

                    heapq.heappush(pq, (newDist, adjNode))

        if dist[n] == float('inf'):
            return [-1]

        path = []
        node = n

        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(1)
        path.reverse()

        path.insert(0, dist[n])

        return path