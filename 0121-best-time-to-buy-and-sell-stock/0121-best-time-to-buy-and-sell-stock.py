class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_return = 0
        
        for i in prices:
            min_price = min(min_price,i)
            max_return = max(max_return, (i - min_price))
        
        return max_return
            
            
        