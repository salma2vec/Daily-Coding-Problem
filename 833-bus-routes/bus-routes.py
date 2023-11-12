class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        queue = deque([(source, 0)])  # (bus stop, number of buses taken)
        visited_stops = {source}
        visited_routes = set()

        while queue:
            current_stop, buses_taken = queue.popleft()

            if current_stop == target:
                return buses_taken

            for route_index in stop_to_routes[current_stop] - visited_routes:
                visited_routes.add(route_index)
                for next_stop in routes[route_index]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))

        return -1        