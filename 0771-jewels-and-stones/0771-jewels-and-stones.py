from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        target = defaultdict(int)
        answer = 0
        
        for i in jewels:
            target[i] += 1
        
        for i in stones:
            if i in target.keys():
                answer += 1
        
        return answer
                
                
        