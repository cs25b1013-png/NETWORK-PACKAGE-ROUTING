def hill_climbing(network_package,source_router,dest_router,heuristic):
    current=source_router
    path=[current]
    visited={current}
    total_weight=0
    expanded=0
    while(current!=dest_router):
        neighbors=network_package.get(current,[])
        best_neighbor=None
        min_h=heuristic.get(current,float('inf'))
        min_weight=float('inf')
        selected_weight=0
        for neighbor,weight in neighbors:
            if neighbor not in visited:
                h_val=heuristic.get(neighbor,float('inf'))
                if(h_val<min_h) or (weight<min_weight and h_val==min_h):
                    min_h=h_val
                    min_weight=weight
                    selected_weight=weight
                    best_neighbor=neighbor

        if best_neighbor is None:
            return None,0,expanded
        current=best_neighbor
        total_weight+=selected_weight
        path.append(current)
        visited.add(current)
        expanded+=1


    return path,total_weight,expanded


if __name__ == "__main__":
    network_package = {
        'Router_A': [('Router_B', 2), ('Router_C', 1)],
        'Router_B': [('Router_A', 2), ('Router_D', 3)],
        'Router_C': [('Router_A', 1), ('Router_D', 1)],
        'Router_D': [('Router_B', 3), ('Router_C', 1), ('Router_F', 2)],
        'Router_F': [('Router_D', 2)]
    }

    heuristic = {
        'Router_A': 5,
        'Router_B': 4,
        'Router_C': 2,
        'Router_D': 1,
        'Router_F': 0
    }

    source_router = 'Router_A'
    dest_router = 'Router_F'

    path, total_weight,expanded = hill_climbing(network_package, source_router, dest_router, heuristic)
    if(path is None):
        print("not found")
        print("expanded nodes:",expanded)
    else:
        print("Computed Route Path:", path)
        print("Total Accumulated Weight:", total_weight)
        print("expanded nodes:",expanded)

        
