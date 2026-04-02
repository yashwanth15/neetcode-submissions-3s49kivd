class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                #invalid base case
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit={} #False=visited, True=visited again in path(invalid case)
        res=[] #store elements in reverse using postorder DFS to avoid incorrect ordering

        def dfs(node):
            #check if the node has been visted previously
            if node in visit:
                #if loop is found return True(visisted in path)
                return visit[node]
            visit[node]=True
            for nei in adj[node]:
                if dfs(nei):
                    return True
            visit[node]=False
            res.append(node)

        for node in adj:
            if dfs(node):
                return ""
        
        res.reverse()
        return "".join(res)


        