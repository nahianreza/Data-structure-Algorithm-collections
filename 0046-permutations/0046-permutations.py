class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def dfs(sol):
            if len(sol) == len(nums):
                res.append(list(sol))

            for j in nums:
                if j not in sol:
                    sol.append(j)
                    dfs(sol)
                    sol.pop()
        
        dfs([])

        return res


        