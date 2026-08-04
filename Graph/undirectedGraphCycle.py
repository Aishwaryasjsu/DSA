from collections import deque
from typing import List
class Solution:
    def bfs(self, i, adj, visited):
        q = deque()
        q.append((i, -1))
        visited[i] = True
        while q:
            node, parent = q.popleft()
            for j in adj[node]:
                if not visited[j]:
                    visited[j]=True
                    q.append((j, node))
                elif j !=parent:
                    return True
        return False

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        cycle=False
        for i in range(V):
            if not visited[i]:
                cycle = self.bfs(i, adj, visited)

                if cycle:
                    break
        return cycle
        