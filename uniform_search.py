import heapq

def uniform_cost_search(network_package, source_router, dest_router):
    frontier = [(0, source_router, [source_router])]
    best_cost = {source_router: 0}
    visited = set()
    expanded = 0

    while frontier:
        cost, current, path = heapq.heappop(frontier)

        if current == dest_router:
            return path, cost, expanded

        if current in visited:
            continue

        visited.add(current)
        expanded += 1

        for neighbor, weight in network_package.get(current, []):
            new_cost = cost + weight

            if neighbor not in visited and new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

    return None, 0, expanded

network_1 = {
    'Router_A': [('Router_B', 2), ('Router_C', 1)],
    'Router_B': [('Router_A', 2), ('Router_D', 3)],
    'Router_C': [('Router_A', 1), ('Router_D', 1)],
    'Router_D': [('Router_B', 3), ('Router_C', 1), ('Router_F', 2)],
    'Router_F': [('Router_D', 2)]
}

network_2 = {
    'Router_A': [('Router_B', 2), ('Router_C', 5)],
    'Router_B': [('Router_A', 2), ('Router_D', 1), ('Router_E', 4)],
    'Router_C': [('Router_A', 5), ('Router_F', 6)],
    'Router_D': [('Router_B', 1), ('Router_F', 2)],
    'Router_E': [('Router_B', 4), ('Router_F', 1)],
    'Router_F': [('Router_C', 6), ('Router_D', 2), ('Router_E', 1)]
}

source_router = 'Router_A'
dest_router = 'Router_F'

for name, network in [("Network 1", network_1), ("Network 2", network_2)]:
    print("---", name, "---")

    path, total_weight, expanded = uniform_cost_search(
        network,
        source_router,
        dest_router
    )

    if path is None:
        print("not found")
        print("expanded nodes:", expanded)
    else:
        print("Computed Route Path:", path)
        print("Total Accumulated Weight:", total_weight)
        print("expanded nodes:", expanded)