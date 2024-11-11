class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        res = []

        def dfs(i):
            if sum(combination) == target:
                res.append(combination.copy())
                return
            if sum(combination) > target or i >= len(candidates):
                return
            
            combination.append(candidates[i])
            dfs(i)

            combination.pop()
            dfs(i+ 1)
        
        dfs(0)

        return res


        