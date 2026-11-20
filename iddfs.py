def iterative_search(network_package,node,dest_router,depth,visited):
    if node==dest_router:
        return [node]
    if depth<=0:
        return None
    visited.add(node)

    for neighbor in network_package.get(node,[]):
        if neighbor not in visited:
            result=iterative_search(network_package,neighbor,dest_router,depth-1,visited)
            if result is not None:
                return [node]+result

    visited.remove(node)
    return None

def iterative_deepning_dfs(network_package,source_router,dest_router,max_depth=10):
    for depth in range(max_depth+1):
        visited=set()
        result=iterative_search(network_package,source_router,dest_router,depth,visited)
        if result is not None:
            return result
    return None

if __name__ == "__main__":
    network_package={'Router_A': [('Router_B', 2), ('Router_C', 5)],
        'Router_B': [('Router_A', 2), ('Router_D', 1), ('Router_E', 4)],
        'Router_C': [('Router_A', 5), ('Router_F', 6)],
        'Router_D': [('Router_B', 1), ('Router_F', 2)],
        'Router_E': [('Router_B', 4), ('Router_F', 1)],
        'Router_F': [('Router_C', 6), ('Router_D', 2), ('Router_E', 1)]}
    source_router='Router_A'
    dest_router='Router_F'
    print(f"Searching route from {source_router} to {dest_router} on a weighted network using IDDFS...")
    shortest_hop_path= iterative_deepning_dfs(network_package,source_router,dest_router,max_depth=10)
    print("Computed Route (Shortest Hop Path):", shortest_hop_path)










