class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        answer = []
        for i in candies:
            temp = i + extraCandies
            if temp >= max_val:
                answer.append(True)
            else:
                answer.append(False)
            
        return answer
        