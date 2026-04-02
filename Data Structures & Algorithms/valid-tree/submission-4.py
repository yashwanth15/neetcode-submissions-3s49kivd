from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create an adjecency list (undirecrted graph)
        # is path set to detect cycle and return False
        # use visited set to skip processed nodes
        # all the nodes should be connected (visited)

        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited=set()
        path=set()
        def dfs(node,parent):
            if node in path:
                return False #cycle detected
            if node in visited:
                return True # skip processed node
            visited.add(node)
            path.add(node)

            for edge in adj[node]:
                if edge==parent:
                    continue #undirected graphs have edges in both directions so skip parent node.
                if not dfs(edge,node):
                    return False # return when cycle is detected
            path.remove(node)
            return True # node processed, return True
        
        if not dfs(0,-1):
            return False
        
        return len(visited)==n
        