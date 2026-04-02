class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #1. create an adjecency list of cources
        #2. do a dfs for all the numCourses
        #3. in dfs use a loop to go through all prerequisites of the course
        #4. use path map to find cycles and return false
        #5. use visited map to skip already processed courses.

        adjecency_list = defaultdict(list)
        for course, prerequisite in prerequisites:
            adjecency_list[course].append(prerequisite)
        
        visited=set() # skip processed courses
        path=set() # detect cycles

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            visited.add(course)
            path.add(course)
            for prerequisite in adjecency_list[course]:
                if not dfs(prerequisite):
                    return False
            path.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        