class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]

        for dep, course in prerequisites:
            adj[course].append(dep)
        
        memo = defaultdict(set)

        def dfs(curr):
            if curr in memo:
                return memo[curr]
                
            curr_deps = set([curr])

            for nei in adj[curr]:
                curr_deps = curr_deps.union(dfs(nei))

            memo[curr] = curr_deps
            return memo[curr]

        for i in range(numCourses):
            dfs(i)  

        res = []
        for u, v in queries:
            if u in memo[v]:
                res.append(True)
            else:
                res.append(False)
        return res
