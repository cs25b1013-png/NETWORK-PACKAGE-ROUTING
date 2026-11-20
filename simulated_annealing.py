import random
import math


def compute_route_weight(network_package, packet_path):
    total_weight = 0
    for i in range(len(packet_path) - 1):
        neighbors = dict(network_package.get(packet_path[i], []))
        total_weight += neighbors[packet_path[i + 1]]
    return total_weight


def sample_initial_route(network_package, source_router, dest_router):
    packet_path = [source_router]
    current_router = source_router

    while current_router != dest_router:
        unvisited_neighbors = [
            neighbor
            for neighbor, _ in network_package.get(current_router, [])
            if neighbor not in packet_path
        ]

        if not unvisited_neighbors:
            return None

        current_router = random.choice(unvisited_neighbors)
        packet_path.append(current_router)

    return packet_path


def simulated_annealing_route(network_package, source_router, dest_router):
    current_path = sample_initial_route(network_package, source_router, dest_router)

    if current_path is None:
        return None

    best_path = current_path[:]
    temperature = 100.0
    all_routers = list(network_package.keys())

    while temperature > 1.0:
        candidate_path = current_path[:]

        if len(candidate_path) > 2:
            pos = random.randint(1, len(candidate_path) - 2)
            candidate_router = random.choice(all_routers)

            if candidate_router not in candidate_path:
                prev_neighbors = dict(network_package.get(candidate_path[pos - 1], []))
                cand_neighbors = dict(network_package.get(candidate_router, []))

                if candidate_router in prev_neighbors and candidate_path[pos + 1] in cand_neighbors:
                    candidate_path[pos] = candidate_router

                    delta = compute_route_weight(network_package, candidate_path) - compute_route_weight(
                        network_package, current_path
                    )

                    if delta < 0 or random.random() < math.exp(-delta / temperature):
                        current_path = candidate_path[:]

                    if compute_route_weight(network_package, current_path) < compute_route_weight(
                        network_package, best_path
                    ):
                        best_path = current_path[:]

        temperature *= 0.95

    return best_path


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

    path = simulated_annealing_route(network_package, source_router, dest_router)

    if path is None:
        print("not found")
    else:
        total_weight = compute_route_weight(network_package, path)
        print("Computed Route Path:", path)
        print("Total Accumulated Weight:", total_weight)