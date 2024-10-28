class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        hmap = {i: [] for i in range(numCourses)}
        visited = set()

        res = []

        for key, val in prerequisites:
            hmap[key].append(val)
        
        def dfs(cur):
            if cur in visited:
                return False
            if hmap[cur] == []:
                if cur not in res:
                    res.append(cur)
                return True
            
            visited.add(cur)

            for pre in hmap[cur]:
                if not dfs(pre):
                    return False
            
            visited.remove(cur)
            hmap[cur] = []
            if cur not in res:
                res.append(cur)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        
        
        return res


        