class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for w in words for c in w}
        # step 1: create adjecency list
        for i in range(len(words)-1):
            first=words[i]
            second=words[i+1]
            minlen=min(len(first),len(second))
            # invalid order of words
            if len(first)>len(second) and first[:minlen]==second[:minlen]:
                return ""

            for j in range(minlen):
                if first[j]!=second[j]:
                    adj[first[j]].add(second[j])
                    break
        
        # step 2: topological sort using dfs in post order traversal
        visited=set()
        path=set() # to detect cycles
        stack=[]
        def topodfs(node):
            if node in path:
                return True
            if node in visited:
                return False
            path.add(node)
            for nei in adj[node]:
                if topodfs(nei):
                    return True
            path.remove(node)
            visited.add(node)
            stack.append(node)
            return False
        
        for node in adj:
            if topodfs(node):
                return ""
        
        stack.reverse()
        return "".join(stack)


        