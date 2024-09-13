class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1
        maxres = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
            
                continue
            if nums[i + 1] - nums[i] == 1:
                res += 1
            else:
                maxres = max(maxres, res)
                res = 1
            
        maxres = max(maxres, res)

        
        return maxres
        