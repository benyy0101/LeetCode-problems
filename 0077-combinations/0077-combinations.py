class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def dfs(elem, start, k):
            if k == 0:
                results.append(elem[:])
                
            for i in range(start,n+1):
                elem.append(i)
                dfs(elem, i + 1, k - 1)
                elem.pop()
            
        dfs([], 1,k)
        return results