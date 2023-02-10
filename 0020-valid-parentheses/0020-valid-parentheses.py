class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["[","{","("]
        close= ["]","}",")"]
        for bracket in s:
            if bracket in open:
                stack.append(bracket)
            elif len(stack) == 0 or open.index(stack.pop()) != close.index(bracket):
                return False
            
        return len(stack) == 0
                
                
            
        