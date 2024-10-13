class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, curList, total):
            if (i >= len(candidates)) or total > target:
                return
            if total == target:
                res.append(list(curList))
                return
            
            
            
            
            curList.append(candidates[i])

            dfs(i, curList, total + candidates[i])

            curList.pop()

            dfs(i + 1, curList, total)
        
        dfs(0, [], 0)
            
        
        return res
            
        