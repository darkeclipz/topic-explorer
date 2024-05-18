---
title: Graphs
---

[Back to index](index.html)

---
# Data Structures
## Graphs

Graphs are a fundamental data structure in computer science and mathematics, widely used to model pairwise relations between objects. Here's a detailed explanation:

### Components of a Graph
1. **Vertex (Node)**: Represents an entity or a point in the graph. Vertices are often named or labeled.
2. **Edge (Link)**: Represents the connection or relationship between two vertices. Edges can be directed or undirected.

### Types of Graphs
- **Undirected Graph**: Edges have no direction. The connection between two vertices is bidirectional.
- **Directed Graph (Digraph)**: Edges have a direction, indicated by an arrow. The connection between vertices is unidirectional.
- **Weighted Graph**: Edges have weights or costs associated with them, useful in finding the shortest path or optimal route.
- **Unweighted Graph**: Edges have no weights; they simply represent connections.
- **Cyclic Graph**: Contains at least one cycle, a path that starts and ends at the same vertex.
- **Acyclic Graph**: Does not contain any cycles.
- **Connected Graph**: There’s a path between any pair of vertices.
- **Disconnected Graph**: At least one pair of vertices is not connected by a path.

### Representations of Graphs
1. **Adjacency Matrix**: A 2D array where a cell (i, j) is true (or contains the edge weight) if there's an edge from vertex i to vertex j.
   - **Pros**: Quick edge lookup (O(1) time complexity).
   - **Cons**: Space-inefficient for sparse graphs.

2. **Adjacency List**: An array of lists/linked lists, where each list contains the neighbors of a specific vertex.
   - **Pros**: Space-efficient for sparse graphs and easier to iterate over neighbors.
   - **Cons**: Edge lookup can take longer (O(V) in the worst case).

3. **Edge List**: A list of all the edges in the graph, where each edge is a pair (or tuple) of vertices.
   - **Pros**: Simple to implement and space-efficient.
   - **Cons**: Edge lookup and neighbor iteration are less efficient.

### Common Operations
1. **Add Vertex**: Add a node to the graph.
2. **Add Edge**: Create a connection between two vertices.
3. **Remove Vertex**: Remove a node and its associated edges.
4. **Remove Edge**: Remove the connection between two vertices.
5. **Search**: Traverse the graph using algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS).
6. **Find Shortest Path**: Use algorithms like Dijkstra's, Bellman-Ford, or A* to find the shortest path in weighted graphs.

### Graph Algorithms
- **Depth-First Search (DFS)**: Explores as far along a branch as possible before backtracking. Uses a stack (recursively or explicitly).
- **Breadth-First Search (BFS)**: Explores all neighbors at the present depth before moving on to nodes at the next depth level. Uses a queue.
- **Dijkstra's Algorithm**: Finds the shortest paths between vertices in a weighted graph with non-negative weights.
- **Bellman-Ford Algorithm**: Computes shortest paths from a single source vertex to all other vertices, even if there are negative weights (detects negative cycles).
- **Floyd-Warshall Algorithm**: Finds shortest paths between all pairs of vertices.
- **Kruskal's Algorithm**: Finds the minimum spanning tree for a connected, undirected graph.
- **Prim's Algorithm**: Also finds the minimum spanning tree, but starts from a specific vertex.

### Use Cases
- **Social Networks**: Vertices can represent users, edges represent friendships or follows.
- **Web Crawling**: Vertices are web pages, edges are hyperlinks.
- **Routing**: Find paths in networks like road maps, communication networks.
- **Scheduling**: Tasks represented as vertices, dependencies as edges.

Understanding graphs, their representations, and various algorithms is crucial in solving complex problems in computer science effectively.

---
[Back to index](index.html)
