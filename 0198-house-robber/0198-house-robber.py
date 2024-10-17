class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            curMax = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = curMax
        
        return rob2