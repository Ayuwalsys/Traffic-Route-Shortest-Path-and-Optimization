
from read_file import read_data_from_file
from convert_graph import convert_to_graph_with_unreachable_nodes
from dijkstra_algorithm import dijkstra_all_shortest_paths
from visualize_Shortestpaths import visualize_shortest_paths_subgraph





# Read data from file
file_path = '/Users/waliuayuba/Documents/Summer_Semester_23/DS5800/Project/5800_project/data/Traffic.csv'  # Replace with the actual file path.
Traffic_data = read_data_from_file(file_path)

# Convert Traffic data to a graph representation
graph = convert_to_graph_with_unreachable_nodes(Traffic_data)

# Define start and end nodes ( points can be changed as needed)
start_node = (771099.088, 2937614.924)
end_node = (770993.9483, 2951341.409)

# Find all shortest paths and the minimum distance
all_shortest_paths, total_distance = dijkstra_all_shortest_paths(graph, start_node, end_node)

print("All Shortest Paths:", all_shortest_paths)
print("Total Distance:", total_distance)


# Visualize the paths
visualize_shortest_paths_subgraph(graph, all_shortest_paths, start_node, end_node)
