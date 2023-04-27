class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        cur = 0
        answer = 0
        
        for i in range(len(prices)):
            if i == 0 or prices[i-1] != prices[i] + 1:
                cur = 0
            cur += 1
            answer += cur
                
            
                
        return answer 
            
        