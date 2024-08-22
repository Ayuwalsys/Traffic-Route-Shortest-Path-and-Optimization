
import networkx as nx
import matplotlib.pyplot as plt

def convert_dict_to_networkx(graph_dict):
    G = nx.Graph()
    for node, neighbors in graph_dict.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    return G

def filter_relevant_nodes(graph, all_shortest_paths, start_node, end_node):
    # Start with nodes in the shortest paths and start/end nodes
    relevant_nodes = set()
    for path in all_shortest_paths:
        relevant_nodes.update(path)
    
    relevant_nodes.add(start_node)
    relevant_nodes.add(end_node)
    
    # Create subgraph with only the relevant nodes
    subgraph = graph.subgraph(relevant_nodes).copy()
    
    return subgraph

def visualize_shortest_paths_subgraph(graph_dict, all_shortest_paths, start_node, end_node):
    # Converting the dictionary to a NetworkX graph
    graph = convert_dict_to_networkx(graph_dict)
    
    # Filtering the graph to get a subgraph with only relevant nodes
    subgraph = filter_relevant_nodes(graph, all_shortest_paths, start_node, end_node)
    
    # Using layout algorithm to position the nodes
    pos = nx.spring_layout(subgraph, seed=42)  # Seed for reproducibility
    
    # Drawing the subgraph
    plt.figure(figsize=(10, 8))
    nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    
    # the shortest paths
    for path in all_shortest_paths:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(subgraph, pos, edgelist=edges, edge_color='red', width=2)
    
    # start and end nodes
    nx.draw_networkx_nodes(subgraph, pos, nodelist=[start_node], node_color='green', node_size=600)
    nx.draw_networkx_nodes(subgraph, pos, nodelist=[end_node], node_color='yellow', node_size=600)
    
    # Show edge weights
    edge_labels = nx.get_edge_attributes(subgraph, 'weight')
    nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=edge_labels, font_color='blue', font_size=8)  # Reduce font size
    
    plt.title(f"Shortest Paths from {start_node} to {end_node}")
    plt.show()

