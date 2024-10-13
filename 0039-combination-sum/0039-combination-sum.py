class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.set = set()

        def dfs(curList):
            if sum(curList) > target:
                return
            tupList = tuple(sorted(curList))
            if sum(curList) == target and tupList not in self.set :
                self.set.add(tupList)
                return
            
            for i in candidates:
                curList.append(i)
                dfs(curList)
                curList.pop()
            
        for c in candidates:
            dfs([c])
        
        
        res = [x for x in self.set]
        return res
            
        