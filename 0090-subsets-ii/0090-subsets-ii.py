class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        sol = []

        def dfs(i):
            if i >= len(nums):
                copy_val = sorted(sol)
                if copy_val not in res:
                    res.append(copy_val)
                return
            
            sol.append(nums[i])
            dfs(i + 1)
            sol.pop()
            dfs(i + 1)

        dfs(0)

        return res
                 
        