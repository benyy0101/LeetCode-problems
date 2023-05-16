class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        p1 = 0
        
        for p2 in t:
            if p2 == s[p1]:
                p1 += 1
            if p1 >= len(s):
                return True
        
        return False
        
    
        
        