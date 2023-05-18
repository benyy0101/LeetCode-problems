class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (right + left) // 2
            temp = 0
            for i in piles:
                con = i // mid
                mod = i % mid

                if con == 0:
                    temp += 1
                elif con != 0 and mod == 0:
                    temp += con
                else:
                    temp += con + 1

            if temp <= h:
                right = mid
            else:
                left = mid + 1
        return left