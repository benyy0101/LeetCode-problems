class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        temp = 0
        for i in nums:
            temp += i
            answer.append(temp)
            
        return answer
            