class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        graph = defaultdict(set)
        

        for bus , route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
            
                    
        queue = deque([(source , 0)])
        visited_stop , visited_bus = {source} , set()
        while queue:
            r  , s = queue.popleft()
            if r == target:
                return s
            for bus in graph[r]:
                if bus not in visited_bus:
                    visited_bus.add(bus)
                    for stop in routes[bus]:
                        if stop not in visited_stop:
                            queue.append((stop, s + 1))
                            visited_stop.add(stop)

        return -1
        