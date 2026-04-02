class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # build an graph of stops with all buses that travel that stop
        graph = collections.defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(i)

        # to find the least no.of buses, we do bfs with (stop, routeLength)
        visitedBuses = set()
        visitedStopes = set()
        q=deque([(source,0)])
        while q:
            stop, routeLength = q.popleft()
            if stop == target:
                # target reached, return route length
                return routeLength
            # find all buses that visit the stop
            for bus in graph[stop]:
                if bus not in visitedBuses:
                    visitedBuses.add(bus)
                    # go to all stops in the bus route
                    for stop in routes[bus]:
                        if stop not in visitedStopes:
                            visitedStopes.add(stop)
                            q.append((stop, routeLength+1))
        
        # target not reached
        return -1

        