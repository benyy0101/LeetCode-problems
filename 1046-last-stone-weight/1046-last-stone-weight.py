import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        qq = []
        
        for i in stones:
            heapq.heappush(qq, -i)
            
        while len(qq) > 1:
            y = heapq.heappop(qq)
            x = heapq.heappop(qq)
            
            
            if x == y:
                continue
            else:
                temp = y - x
                heapq.heappush(qq, temp)
                
        if len(qq) == 0:
            return 0
        else:
            return -qq[0]
            
        
        