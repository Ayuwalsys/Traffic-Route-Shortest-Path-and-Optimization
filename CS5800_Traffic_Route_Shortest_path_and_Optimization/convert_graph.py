def convert_to_graph_with_unreachable_nodes(data):
    # Initialize an empty dictionary for the graph
    graph = {}
    
    # Ensuring all nodes are in the graph, even if with no connections
    all_nodes = set(data["X1"].combine(data["Y1"], lambda x, y: (x, y)))
    all_nodes.update(set(data["X2"].combine(data["Y2"], lambda x, y: (x, y))))
    
    for node in all_nodes:
        if node not in graph:
            graph[node] = {}

    #add the edges
    for _, row in data.iterrows():
        # Extracting node coordinates and the distance between them
        a_node = (row["X1"], row["Y1"])
        b_node = (row["X2"], row["Y2"])
        distance = row["Dist"]
        
        # Add edges between a_node and b_node
        graph[a_node][b_node] = distance
        graph[b_node][a_node] = distance
    
    return graph
