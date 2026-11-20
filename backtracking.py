def backtracking_route(network_package, current_router, dest_router, packet_path):
    if current_router == dest_router:
        return packet_path

    for neighbor, _ in network_package.get(current_router, []):
        if neighbor not in packet_path:
            result = backtracking_route(
                network_package, neighbor, dest_router, packet_path + [neighbor]
            )
            if result:
                return result

    return None


def get_path_weight(network_package, packet_path):
    total_weight = 0
    for i in range(len(packet_path) - 1):
        neighbors = dict(network_package.get(packet_path[i], []))
        total_weight += neighbors[packet_path[i + 1]]
    return total_weight


if __name__ == "__main__":
    network_package = {
        'Router_A': [('Router_B', 2), ('Router_C', 1)],
        'Router_B': [('Router_A', 2), ('Router_D', 3)],
        'Router_C': [('Router_A', 1), ('Router_D', 1)],
        'Router_D': [('Router_B', 3), ('Router_C', 1), ('Router_F', 2)],
        'Router_F': [('Router_D', 2)]
    }

    source_router = 'Router_A'
    dest_router = 'Router_F'

    path = backtracking_route(network_package, source_router, dest_router, [source_router])

    if path is None:
        print("not found")
    else:
        total_weight = get_path_weight(network_package, path)
        print("Computed Route Path:", path)
        print("Total Accumulated Weight:", total_weight)