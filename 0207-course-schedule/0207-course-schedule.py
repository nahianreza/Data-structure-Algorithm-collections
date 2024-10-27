class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {i: [] for i in range(numCourses)}


        for key,val in prerequisites:
            hmap[key].append(val)

        visited = set()
        def dfs(cur):
            if cur in visited:
                return False
            if hmap[cur] == []:
                return True
            
            visited.add(cur)

            for pre in hmap[cur]:
                if not dfs(pre):
                    return False
            
            visited.remove(cur)
            hmap[cur] = []

            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        
        