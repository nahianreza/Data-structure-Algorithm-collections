class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        for i in nums:
            minVal = min(minVal, i)
        return minVal
        