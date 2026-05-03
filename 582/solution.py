class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        if kill == 0:
            return pid

        adj = defaultdict(list)

        for idx, parent in enumerate(ppid):
            if parent != 0:
                adj[parent].append(pid[idx])

        res = [] 
        seen = set()
        def dfs(curr):
            if curr not in seen:
                seen.add(curr)
                res.append(curr)
                for child in adj[curr]:
                    dfs(child)
        
        dfs(kill)
        return res
