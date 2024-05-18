---
title: Graph Theory
---

[Back to index](index.html)

---
# Discrete Mathematics
## Graph Theory

Graph Theory is a branch of discrete mathematics that studies graphs, which are mathematical structures used to model pairwise relations between objects. Here's an overview of key concepts within graph theory:

### Basic Concepts:
1. **Graph**: A graph \( G = (V, E) \) consists of a set of vertices (or nodes) \( V \) and a set of edges \( E \) where each edge is a pair of vertices.

2. **Vertex (Node)**: A fundamental unit (point) in a graph.

3. **Edge**: A connection (line) between two vertices. Edges can be directed (having a direction from one vertex to another) or undirected.

4. **Adjacency**: Two vertices are adjacent if they are connected by an edge.

5. **Degree**: The degree of a vertex is the number of edges incident to it. For directed graphs, we distinguish between in-degree (incoming edges) and out-degree (outgoing edges).

### Types of Graphs:
1. **Undirected Graph**: Edges have no direction, i.e., if there's an edge between \( v_1 \) and \( v_2 \), you can move in both directions.

2. **Directed Graph (Digraph)**: Edges have direction, i.e., if there's an edge from \( v_1 \) to \( v_2 \), you can only move from \( v_1 \) to \( v_2 \).

3. **Weighted Graph**: Edges have weights assigned to them, representing costs, lengths, or capacities.

4. **Simple Graph**: A graph with no loops (edges connected at both ends to the same vertex) and no multiple edges between the same pair of vertices.

5. **Complete Graph**: A graph in which every pair of vertices is connected by a unique edge.

6. **Bipartite Graph**: A graph whose vertices can be divided into two disjoint sets such that no two graph vertices within the same set are adjacent.

### Special Graphs and Structures:
1. **Tree**: An undirected graph in which any two vertices are connected by exactly one path. Trees have no cycles.

2. **Cycle**: A path of edges and vertices wherein a vertex is reachable from itself.

3. **Path**: A sequence of edges where the end vertex of one edge is the start vertex of the next; also, all vertices are distinct.

4. **Subgraph**: A graph formed from a subset of the vertices and edges of another graph.

### Key Problems and Algorithms:
1. **Shortest Path Problem**: Find the shortest path between two vertices. Common algorithms include Dijkstra's and Bellman-Ford algorithms.

2. **Minimum Spanning Tree**: Find a subset of edges that connect all vertices with the minimum possible total edge weight. Common algorithms include Kruskal's and Prim's algorithms.

3. **Graph Coloring**: Assign colors to vertices so that no two adjacent vertices share the same color, with the aim of minimizing the number of colors.

4. **Network Flow**: Determine the maximum flow possible from a source to a sink in a network. The Ford-Fulkerson algorithm is commonly used.

5. **Graph Isomorphism**: Determine whether two graphs are isomorphic, meaning they contain the same number of graph vertices connected in the same way.

### Applications:
Graph theory has wide applications in various fields including computer science (social networks, internet modeling), biology (ecological networks, neural networks), engineering (circuit design), logistics (transportation networks), and many other domains involving relational data.

Understanding graph theory is fundamental for solving problems related to networks, optimizing paths, and understanding the structure and behavior of interconnected systems.

---
[Back to index](index.html)
