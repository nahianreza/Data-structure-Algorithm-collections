class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        total = 0
        res, temp = 0, prices[0]

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                total += prices[r] - prices[l]
                
            l = r
        
        return total

        