def revise_router_domain(network_package, router_domains, slot_i, slot_j):
    revised = False

    for router_x in router_domains[slot_i][:]:
        valid = False
        neighbors_x = dict(network_package.get(router_x, []))

        for router_y in router_domains[slot_j]:
            if router_y in neighbors_x and router_x != router_y:
                valid = True
                break

        if not valid:
            router_domains[slot_i].remove(router_x)
            revised = True

    return revised


def ac3_route_domains(network_package, router_domains):
    queue = []

    for i in range(len(router_domains) - 1):
        queue.append((i, i + 1))
        queue.append((i + 1, i))

    while queue:
        slot_i, slot_j = queue.pop(0)

        if revise_router_domain(network_package, router_domains, slot_i, slot_j):
            if len(router_domains[slot_i]) == 0:
                return False

            for slot_k in range(len(router_domains)):
                if abs(slot_k - slot_i) == 1 and slot_k != slot_j:
                    queue.append((slot_k, slot_i))

    return True


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
    hop_count = 3

    router_domains = [list(network_package.keys()) for _ in range(hop_count + 1)]
    router_domains[0] = [source_router]
    router_domains[hop_count] = [dest_router]

    if ac3_route_domains(network_package, router_domains):
        print("Arc consistency maintained")
        print("Possible routers at each position:")
        for i in range(len(router_domains)):
            print("Hop", i, ":", router_domains[i])
    else:
        print("not found")