class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, value in enumerate(nums):
            missedNum = target - value
            if missedNum in dict:
                return [i, dict[missedNum]]

            dict[value] = i