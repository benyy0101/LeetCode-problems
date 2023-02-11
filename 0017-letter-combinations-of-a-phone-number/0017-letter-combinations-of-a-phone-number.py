class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        length = len(digits)
        answer = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def dfs(depth,target):
            if depth == length:
                answer.append(target)
                return
            
            else:
                alphs = phone[digits[depth]]
                
                for i in alphs:
    
                    dfs(depth + 1, target + i)
                    
        
        
        
        dfs(0,"")
        
        return answer
                
                
        