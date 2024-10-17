class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[7,1,5,3,6,4]
        largestDiff = 0
        min = 10000
        for x in range(len(prices)):
            if(prices[x]< min):
                min = prices[x]
            else:
                largestDiff = max(largestDiff,prices[x] - min)
        return largestDiff


        