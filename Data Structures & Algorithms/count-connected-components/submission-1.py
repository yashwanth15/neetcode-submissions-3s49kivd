class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # parent of each node is itself
        parent=list(range(n))
        components=n
        rank=[0]*n

        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x

        def union(a,b):
            pa=find(a)
            pb=find(b)

            #already connected
            if pa==pb:
                return False
            
            if rank[pa]<rank[pb]:
                parent[pa]=pb
            elif rank[pb]<rank[pa]:
                parent[pb]=pa
            else:
                parent[pa]=pb
                rank[pb]+=1
            return True
        
        for a,b in edges:
            if union(a,b):
                components-=1
        
        return components

            
        