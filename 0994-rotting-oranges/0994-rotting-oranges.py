class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:       
        m=len(grid)
        n=len(grid[0])
        def check():
            for i in range(m):
                if 1 in grid[i]:
                    return 1
        if not check():
            return 0
        t=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j,0])
        while len(q)>0:
            a,b,t=q.popleft()
            if b>0 and grid[a][b-1]==1:#left
                grid[a][b-1]=2
                q.append([a,b-1,t+1])
            if b<n-1 and grid[a][b+1]==1:#right
                grid[a][b+1]=2
                q.append([a,b+1,t+1])
            if a>0 and grid[a-1][b]==1:#up
                grid[a-1][b]=2
                q.append([a-1,b,t+1])
            if a<m-1 and grid[a+1][b]==1:#down
                grid[a+1][b]=2
                q.append([a+1,b,t+1])
        if check():
            return -1
        return t