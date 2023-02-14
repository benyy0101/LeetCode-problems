from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        route = defaultdict(list)
        tickets.sort(reverse=True)
        answer = []
        
        for x,y in tickets:
            route[x].append(y)
        
        def dfs(des):
            while route[des]:
                target = route[des].pop()
                dfs(target)
            answer.append(des)
                
        dfs("JFK")
        
        return answer[::-1]
                
                
            
        
            
        