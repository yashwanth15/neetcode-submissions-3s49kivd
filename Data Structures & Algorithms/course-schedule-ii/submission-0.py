class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # same as course scedule 1 + add the course after processing it.
        adj=defaultdict(list)
        visited=set()
        path=set()
        order_of_courses=[]

        for cr,pr in prerequisites:
            adj[cr].append(pr)
        
        def dfs(cr):
            if cr in path:
                return False #cycle detected
            if cr in visited:
                return True #skip processed node
            
            visited.add(cr)
            path.add(cr)
            for pr in adj[cr]:
                if not dfs(pr):
                    return False
            path.remove(cr)
            order_of_courses.append(cr)
            return True
        
        for cr in range(numCourses):
            if not dfs(cr):
                return []
        
        return order_of_courses
