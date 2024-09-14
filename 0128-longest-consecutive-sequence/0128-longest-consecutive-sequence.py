class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        res = 0
        maxRes = 0

        for i in newSet:
            if (i-1) not in newSet:
                val = i
                res = 0
                while val in newSet:
                    val += 1
                    res += 1
                
                maxRes = max(res, maxRes)
            else:
                continue
                
        
        
        
        return maxRes
