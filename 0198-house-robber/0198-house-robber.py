class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            cur = max(i + rob1, rob2)
            rob2, rob1 = cur, rob2
        
        return rob2
        


        