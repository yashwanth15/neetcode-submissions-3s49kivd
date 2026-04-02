class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #build adjecency list with u->current course, v->prerequisite
        graph={i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            graph[u].append(v)

        #state: 0-> not visited, 1-> in the path, 2-> path is completed
        state = [0]*numCourses

        def dfs(u):
            if state[u]==1:
                # cycle detected
                return False
            if state[u]==2:
                return True
            
            state[u]=1
            for v in graph[u]:
                if not dfs(v):
                    return False
            # course explored, can be completed
            state[u]=2
            return True
            
        #there can be multiple graphs so dfs over all the courses.
        for u in range(numCourses):
            if not dfs(u):
                return False
        return True
