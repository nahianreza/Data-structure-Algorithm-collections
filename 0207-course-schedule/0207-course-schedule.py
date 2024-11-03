class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(list)

        for key, val in prerequisites:
            courses[key].append(val)

        visited = set()
        
        def dfs(cur):
            if cur in visited:
                return False
            if courses[cur] == []:
                return True
            
            visited.add(cur)

            neighbors = courses[cur]

            for n in neighbors:
                if not dfs(n):
                    return False

            courses[cur] = []
            visited.remove(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        

        
        