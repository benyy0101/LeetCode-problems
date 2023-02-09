from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        target = Counter(nums)
        result = []
        for num, cnt in target.items():
            result.append([num,cnt])
        result.sort(key= lambda x: -x[1])
        answer = []
        for i in range(k):
            answer.append(result[i][0])
            
        return answer
            
        
       
        
        