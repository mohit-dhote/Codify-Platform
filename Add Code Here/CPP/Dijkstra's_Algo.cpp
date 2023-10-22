#include <iostream>
#include <vector>
#include <limits>

#define INF std::numeric_limits<int>::max()

// Function to find the vertex with the minimum distance value, from the set of vertices not yet included in the shortest path tree
int minDistance(const std::vector<int> &dist, const std::vector<bool> &sptSet, int V) {
    int min = INF;
    int min_index;
    for (int v = 0; v < V; ++v) {
        if (!sptSet[v] && dist[v] <= min) {
            min = dist[v];
            min_index = v;
        }
    }
    return min_index;
}

// Function to print the constructed distance array
void printSolution(const std::vector<int> &dist, int V) {
    std::cout << "Vertex \t\t Distance from Source" << std::endl;
    for (int i = 0; i < V; ++i) {
        std::cout << i << " \t\t " << dist[i] << std::endl;
    }
}

// Function that implements Dijkstra's single source shortest path algorithm for a graph represented using adjacency matrix representation
void dijkstra(const std::vector<std::vector<int>> &graph, int src, int V) {
    std::vector<int> dist(V, INF); // The output array. dist[i] will hold the shortest distance from src to i

    std::vector<bool> sptSet(V, false); // sptSet[i] will be true if vertex i is included in the shortest path tree

    dist[src] = 0; // Distance of source vertex from itself is always 0

    for (int count = 0; count < V - 1; ++count) {
        int u = minDistance(dist, sptSet, V); // Pick the minimum distance vertex from the set of vertices not yet processed
        sptSet[u] = true; // Mark the picked vertex as processed

        // Update dist value of the adjacent vertices of the picked vertex
        for (int v = 0; v < V; ++v) {
            if (!sptSet[v] && graph[u][v] && dist[u] != INF && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    printSolution(dist, V);
}

// Main function
int main() {
    std::vector<std::vector<int>> graph = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
                                          {4, 0, 8, 0, 0, 0, 0, 11, 0},
                                          {0, 8, 0, 7, 0, 4, 0, 0, 2},
                                          {0, 0, 7, 0, 9, 14, 0, 0, 0},
                                          {0, 0, 0, 9, 0, 10, 0, 0, 0},
                                          {0, 0, 4, 14, 10, 0, 2, 0, 0},
                                          {0, 0, 0, 0, 0, 2, 0, 1, 6},
                                          {8, 11, 0, 0, 0, 0, 1, 0, 7},
                                          {0, 0, 2, 0, 0, 0, 6, 7, 0}};

    dijkstra(graph, 0, 9);

    return 0;
}
