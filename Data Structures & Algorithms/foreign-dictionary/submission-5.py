class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for w in words for c in w}
        indegree={ch:0 for ch in adj}
        order=[]
        # step 1: create adjecency list
        for i in range(len(words)-1):
            first=words[i]
            second=words[i+1]
            minlen=min(len(first),len(second))
            # invalid order of words
            if len(first)>len(second) and first[:minlen]==second[:minlen]:
                return ""

            for j in range(minlen):
                a= first[j]
                b= second[j]
                if a!=b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indegree[b]+=1
                    break
        
        # step 2: topological sort using bfs (Khans algorithm)
        q=deque([ch for ch in indegree if indegree[ch]==0])

        while q:
            ch = q.popleft()
            order.append(ch)
            for nei in adj[ch]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        # setep 3: cycle check
        if len(adj)!=len(order):
            return ""
        
        return "".join(order)



        