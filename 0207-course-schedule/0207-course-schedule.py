from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            edge = prerequisites[i]
            adjList[edge[0]].append(edge[1])

        for v in range(numCourses):
            if len(adjList[v]) == 0:
                continue

            q = deque(adjList[v])
            visited = set()
            
            while q:
                u = q.pop()
                visited.add(u)
                
                if u == v:
                    return False
                
                for n in adjList[u]:
                    if n not in visited:
                        q.appendleft(n)
                
            adjList[v] = []

        return True
                
            
                
            
            