class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        sol = []

        def dfs(i):
            if i >= len(nums):
                if sol not in res:
                    res.append(sol.copy())
                return
            
            sol.append(nums[i])
            dfs(i + 1)
            sol.pop()
            dfs(i + 1)

        dfs(0)

        return res
                 
        