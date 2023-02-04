from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            start, end = i + 1, len(nums)-1
            
            while start < end:
                sum = nums[start] + nums[end] + nums[i]
                if sum < 0:
                    
                    start += 1
                elif sum > 0:
                    
                    end -= 1
                else:
                    result.append([nums[i],nums[start],nums[end]])
                    
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
        return result