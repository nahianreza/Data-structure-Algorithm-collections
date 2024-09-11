class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        sets = []

        def dfs(index):
            if index >= len(nums):
                res.append(sets.copy())
                return
            
            sets.append(nums[index])
            dfs(index + 1)

            sets.pop()
            dfs(index + 1)
        
        dfs(0)
        return res