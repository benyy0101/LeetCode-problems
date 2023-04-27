class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []
        
        for case in spells:
            start = 0
            end = len(potions) - 1
            
            while start <= end:
                mid = (start + end) // 2
                if potions[mid] * case >= success:
                    end = mid - 1
                else:
                    start = mid + 1
                    
            result = len(potions) - start
            answer.append(result)
            
        return answer
        