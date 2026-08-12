#include <bits/stdc++.h>
using namespace std;

// Traversing Algorithms:

void dfs(vector<vector<int>>& adj, vector<int>& visited, int node)
{
    visited[node] = true;
    for(int adjNode:adj[node])
    {
        if(visited[adjNode]) continue;
        dfs(adj, visited, adjNode);
    }
}

void bfs(vector<vector<int>>& adj, int src)
{
    int n = adj.size();
    vector<int> visited(n);
    visited[src] = 1;
    queue<int> q;
    q.push(src);
    while(!q.empty())
    {
        int node = q.front();
        q.pop();
        for(int adjNode:adj[node])
        {
            if(visited[adjNode]) continue;
            visited[adjNode] = 1;
            q.push(adjNode);
        }
    }
}

// disjoint

// Problems On Traversals:

// Number Of Provinces: https://practice.geeksforgeeks.org/problems/number-of-provinces/1

// Number Of Islands: https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1

// Flood Fill: https://practice.geeksforgeeks.org/problems/flood-fill-algorithm1856/1

// Rotten Oranges: https://practice.geeksforgeeks.org/problems/rotten-oranges2536/1

// Distance Of Nearest 1: https://practice.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1

// Replace O's With X's: https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1

// Number Of Enclave: https://practice.geeksforgeeks.org/problems/number-of-enclaves/1

// Number of Distinct Islands: https://practice.geeksforgeeks.org/problems/number-of-distinct-islands/1

// Bipartite Graph: a graph which can be colored using two colors such no adjacent node have the same color. Linear graphs i.e tree like graphs are always bipartite. Graphs with even length cycles are also bipartite. Graphs with odd length cycle are not bipartite. To check whether a graph is bipartite or not we can use dfs or bfs, we color the starting node from some color, then during the traversal we color not visited nodes with color different from color of current node, and for visited nodes we check their color, if it is same as our color then we return false, or continue traversing.