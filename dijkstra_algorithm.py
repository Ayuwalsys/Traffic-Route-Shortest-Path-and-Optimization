import heapq
from collections import defaultdict

def dijkstra_all_shortest_paths(graph, start_node, end_node):
    # Initialized dictionaries to store paths and shortest distances
    distance_dict = {node: float('inf') for node in graph}
    distance_dict[start_node] = 0
    paths_dict = defaultdict(list)
    paths_dict[start_node] = [[start_node]]
    
    # Priority queue to store nodes for evaluation
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # process skipped if the current path is not optimal
        if current_distance > distance_dict[current_node]:
            continue

        # Evaluate the neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distance_dict[neighbor]:
                # Found a shorter path, update distance and paths
                distance_dict[neighbor] = distance
                paths_dict[neighbor] = [path + [neighbor] for path in paths_dict[current_node]]
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distance_dict[neighbor]:
                # Found an equally short path, add the path to the paths list
                paths_dict[neighbor].extend([path + [neighbor] for path in paths_dict[current_node]])

    # Return all shortest paths, their distance
    return paths_dict[end_node], distance_dict[end_node]