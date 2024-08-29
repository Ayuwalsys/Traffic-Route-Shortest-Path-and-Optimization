# Traffic-Route-Shortest-Path-and-Optimization

## Overview

This repository contains the code and data for the final project proposal titled **"Traffic Route Shortest Path and Optimization"**. The project was developed as part of the CS5800 course in Summer 2023. The main goal of this project is to optimize traffic routes in the city of Boston by implementing and analyzing Dijkstra's algorithm for finding the shortest path in a road network.

## Project Context

Each day, hundreds of thousands of people in Boston travel by car or transit. The time spent at traffic signals can add up, leading to long and inefficient commutes. This project aims to address this problem by developing a route optimization algorithm that minimizes travel time, reduces emissions, and improves overall transportation efficiency. The research also explores the applicability of Dijkstra's algorithm in real-time traffic management systems.

## Features

- **Dijkstra's Algorithm Implementation**: Efficient computation of the shortest path between two locations.
- **Traffic Data Processing**: Conversion of traffic data into a graph representation for use in the algorithm.
- **Visualization of Shortest Paths**: Tools to visualize the computed shortest paths on a map.
- **Real-Time Traffic Optimization**: Consideration of dynamic traffic conditions in route optimization.

## Files

- **`CS5008 Final project proposal.pdf`**: The project proposal document outlining the problem context, research question, and scope of the project.
- **`dijkstra_algorithm.py`**: Python script implementing Dijkstra's algorithm to find the shortest path in a graph representing the road network.
- **`visualize_Shortestpaths.py`**: A script for visualizing the computed shortest paths using the matplotlib library.
- **`convert_graph.py`**: A script to convert traffic data into a graph structure suitable for shortest path computations.
- **`read_file.py`**: A utility script for reading and preprocessing the traffic data from CSV files.
- **`main.py`**: The main script that ties together the data processing, algorithm implementation, and visualization.
- **`Traffic.csv`**: The dataset containing traffic signal information in the city of Boston, used as input for the optimization algorithms.

## Requirements

- Python 3.8 or higher
- Required Python packages:
  - `matplotlib`
  - `networkx`
  - `pandas`
  - `numpy`

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## How to Run

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the `main.py` script to perform the shortest path computations and visualize the results:

```bash
python main.py
```

## Contributions

This project was developed by Waliu Ayuba, Cristina Stone Pedraza, Dhruv Miyani, and Jaimeen Yogesh Kumar Unagar as part of the CS5800 Final Project.

