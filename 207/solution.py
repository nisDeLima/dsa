class Solution: 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for course, dep in prerequisites:
            adj[course].append(dep)
        
        can_complete = set()
        checking = set()

        def dfs(course):
            if course in can_complete:
                return True
            if course in checking:
                return False
            
            checking.add(course)
            for dep in adj[course]:
                if not dfs(dep):
                    return False

            can_complete.add(course)
            checking.remove(course)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
