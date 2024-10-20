class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        res = -float('inf')
        maxVal = 0

        for r in range( len(nums)):
            if maxVal < 0:
                maxVal = 0
            maxVal += nums[r]

            res = max(res, maxVal)

        return res
            

