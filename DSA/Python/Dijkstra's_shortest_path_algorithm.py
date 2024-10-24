# Python program for Dijkstra's shortest path algorithm

import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        # Initialize graph as an adjacency matrix
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        # Print the shortest distances from source
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        # Find the vertex with the minimum distance not in the shortest path tree
        min = sys.maxsize
        for u in range(self.V):
            if dist[u] < min and not sptSet[u]:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        # Initialize distances and shortest path tree set
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            # Pick the minimum distance vertex
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True  # Add to shortest path tree

            # Update distances of adjacent vertices
            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)

# Driver's code
if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    
    g.dijkstra(0)  # Run Dijkstra's algorithm from source vertex 0
