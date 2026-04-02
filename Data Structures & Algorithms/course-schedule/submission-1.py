class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to its prerequisites
        preMap={i:[] for i in range(numCourses)}
        for cr,pr in prerequisites:
            preMap[cr].append(pr)
        #store all the courses along the current DFS path
        visited=set()

        def dfs(cur):
            if cur in visited:
                #cycle detected
                return False
            if preMap[cur]==[]:
                return True
            visited.add(cur)
            for i in preMap[cur]:
                if not dfs(i): return False
            visited.remove(cur)
            preMap[cur]=[]
            return True
        
        #there can be multiple graphs so dfs over all the courses.
        for cur in range(numCourses):
            if not dfs(cur): return False
        return True
