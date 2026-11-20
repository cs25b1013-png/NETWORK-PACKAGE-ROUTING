def dfs_route(network_package, source, destination):
    stack = [(source, [source])]
    visited = set()

    while stack:
        router, path = stack.pop()

        if router == destination:
            return path

        if router in visited:
            continue

        visited.add(router)

        for neighbor, cost in network_package[router]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


network_package = {
    'Router_A': [('Router_B', 2), ('Router_C', 1)],
    'Router_B': [('Router_A', 2), ('Router_D', 3)],
    'Router_C': [('Router_A', 1), ('Router_D', 1)],
    'Router_D': [('Router_B', 3), ('Router_C', 1), ('Router_F', 2)],
    'Router_F': [('Router_D', 2)]
}

source_router = 'Router_A'
dest_router = 'Router_F'

path = dfs_route(network_package, source_router, dest_router)

if path:
    print("DFS Route:", " -> ".join(path))
else:
    print("No route found")