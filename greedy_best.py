import heapq
def greedy_best(network_package,source_router,dest_router,heuristic):
    pq=[]
    start_h=heuristic.get(source_router,float('inf'))
    heapq.heappush(pq,(start_h,source_router,[source_router],0))
    visited=set()
    expanded=0
    while pq:
        h_val,current,path,total_cost=heapq.heappop(pq)
        h_val=heuristic.get(current,float('inf'))
        if current==dest_router:
            return path,total_cost,expanded
        if current in visited:
            continue
        visited.add(current)
        expanded+=1

        for neighbor,weight in network_package.get(current,float('inf')):
            if neighbor not in visited:
                h_val=heuristic.get(neighbor,float('inf'))
                heapq.heappush(pq,(h_val,neighbor,path+[neighbor],total_cost+weight))

    return None,float('inf'),expanded

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

    path,total_cost,expanded = greedy_best(network_package, source_router, dest_router, heuristic)

    if path is None:
        print("not found")
        print("nodes expanded:",expanded)
    else:
    
        print("Optimal Route Path:", path)
        print("Total Path Cost:", total_cost)
        print("nodes expanded:",expanded)



   

