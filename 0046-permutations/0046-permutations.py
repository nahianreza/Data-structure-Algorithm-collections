class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = []

        def dfs(cur):
            if len(permutations) == len(nums):
                res.append(permutations.copy())
                return
            
            for p in nums:
                if p not in permutations:
                    permutations.append(p)
                    dfs(p)
                    permutations.pop()
        
        dfs(nums[0])

        return res

        