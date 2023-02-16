class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        answer = [intervals[0]]
        
        for start, end in intervals:
            temp = answer[-1][1]
            
            if start <= temp:
                answer[-1][1] = max(temp, end)
            else:
                answer.append([start,end])
                
        return answer
        
        
             
            