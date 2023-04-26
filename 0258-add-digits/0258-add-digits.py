class Solution:
    def addDigits(self, num: int) -> int:
        
        temp = list(str(num))
        
        while True:
            answer = sum(map(int,temp))
            if len(str(answer)) == 1:
                return answer
            else:
                temp = list(str(answer))
        
        
        
        
            
            