class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #adjecency list
        adj={i:[] for i in range(n)}
        for a,b in edges:
            #undirected graph points both ways
            adj[a].append(b)
            adj[b].append(a)
        
        visit=set()

        def dfs(cur,prev):
            if cur in visit:
                #cycle detected
                return False
            
            visit.add(cur)
            for node in adj[cur]:
                # skip the false positive of a loop, becuase in an undirected graph each node points both ways.
                if node == prev:
                    continue
                if not dfs(node,cur): return False
            return True
        
        #detect if there are loops and if there are multiple graphs
        return dfs(0,-1) and len(visit)==n
        