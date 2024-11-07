class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def totalRob(nums):
            rob1, rob2 = 0, 0

            for i in nums:
                temp = max(rob1 + i, rob2)
                rob2, rob1 = temp, rob2

            return rob2
        
        return max(totalRob(nums[1:]), totalRob(nums[:len(nums) - 1]))

        



              

        