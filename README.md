# national-airspace-system
## Simplified model of the National Airspace System

## Problem ##
Given a data set with flights, calculate the maximum number of passengers that can travel from the source to the destination in 24 hours from 0:00 to 23:59.

## Constraints ##
- A passenger can only travel from LAX to JFK
- For multi-stop flights, the arrival time from a flight must be <= the departure time of the next flight
- If the capacity in an edge holds true for at least one passenger, then the capacity of the system is at least 1

## Understanding the problem ##
In the dataset, there are 5 values given: source airport, destination airport, departure time, arrival time, and flight capacity of each flight. In order to find the maximum number of passengers, I believed it would be best to create a graph data structure representing the vertices as combined airport/time and the edges as the flight capacity.

Where G is a directed graph:
- G = (V,E) where V is a set of vertices and E is a set of edges
- {V} = [(source airport, departing time), (destination airport, arrival time),...]
- {E} = [(((source airport, departing time), (destination airport, arrival time)):flight capacity),...]

Given the data set flights.csv where 722 flights are given, I’ve calculated a total of 321 unique vertices and 722 edges.

Graph visualized with Python Networkx library:





After constructing a graph with such vertices, and the edges holding their flight capacities, the graph is now ready to be used to calculate the maximum flow in consideration of the constraints. As LAX is the starting airport and JFK is the ending airport, we know that flights can travel between any of the airports in any amount of time as long as:

starting vertice "start" = any vertices containing LAX
i.e (LAX, 0) or (LAX,10)
ending vertice "sink" = any vertices containing JFK
I.e (JFK,7) or (JFK,14)

Since in my graph each vertice is paired up with their designated start or end time, we know there will be more than one of each airport if the data set contains an airport with more than one start or end time. For simplicity, in the figure above, each start is colored green, each sink is colored red, and all other internal nodes are blue. Edge labels displaying the capacity have been turned off in this image for better visualization.

# Approach
To calculate the maximum number of passengers: begin each path at the start vertex and traverse over the graph. In each path,  I will prioritize filling my flights with as many passengers my edge allows by using a greedy approach when selecting which edge to take:
Choose the earliest available flight/edge, as long as it satisfies the condition of time regarding the next departing flight
Choosing the largest available flight/edge capacity, as long as it adheres to the bottleneck capacity of the path 

By using this approach exhaustively, I can calculate the maximum number of passengers that can be pushed from the start to the sink of each path. Since paths can use any edge available to them during their decision making, which may include going to a "previous” vertex which would be considered backward labeling. Allowing for backward labeling allows for passengers to take different routes/edges and utilize other capacities for the maximum achievable flow result. Thus, the algorithm best for calculating the maximum number of passengers would be to use the max-flow min-cut algorithm, Ford Fuklerson, which uses a greedy-approach in every local decision to find the maximum flow solution for the entire graph. In this problem, I will be referring to the passengers as flow in our network, and the network as our directed graph.

# Steps
Create a directed graph G=(V,E)
Traverse through G and set all initial flow to 0, marking start as labeled and other internal and sink vertices as unlabeled 
Find all possible paths from LAX to JFK by traversing through G with bfs
To find a path: find a vertex that’s unlabeled and mark it once it has been accessed in a path
During a pathfinding, use the greedy approach of selecting:
the edge available with the largest available flight capacity
the vertice with the earliest departing time in order to have as many flight make it to the end before the 24hrs
in this step, always check for the conditional case: if destination arrival time is <= departing time
Once a path is found and a path is at the sink, backtrack by following the labels that you’ve previously marked to s. 
If all edges have been labeled, halt.
Maximum flow (maximum amount of passengers that can make it from LAX to JFK in 24hrs) += "path flow" (each path's bottleneck capacity/how many passengers a path carried at a time)

Time/Space Complexity
Project still in progress.  

