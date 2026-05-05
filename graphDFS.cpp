/*
Let G = (V,E) be a directed graph in which each vertex u in V is labeled with a unique 
integer L(u) from the set {1,2,...|V|}. For each vertex u in V , let R(u)= {v in V:  u -->v} 
be the set of vertices that are reachable from u. Define min(u) to be the vertex in R(u) 
whose label is minimum, i.e. min(u) is the vertex v such that L(v) = min{L(w): w in R(u)}. 
Implement an O(V+E)-time algorithm that computes min(u) for all vertices u in V. Show 
that your algorithm is correct using different test cases 
*/

#include <iostream>
#include <vector>

using namespace std;

void dfs(int u, vector<vector<int>>& adj, vector<int> &label, vector<int> &minVertex, vector<bool>& visited);

int main(){

    //TC: O(V+E) as we are performing DFS

    
    int v = 5; 
    vector<vector<int>> adj = {{1,2},{3},{3},{4},{}}; 
    vector<int> label = {4,1,5,3,2}; 
    vector<int> minVertex(v, -1);  
    vector<bool> visited(v, false);

    // int v = 6; 
    // vector<vector<int>> adj = {{1}, {2, 3}, {0}, {4}, {5, 1}, {}}; 
    // vector<int> label = {8, 3, 7, 2, 5, 1}; 
    // vector<int> minVertex(v, -1);  
    // vector<bool> visited(v, false);


    // int v = 7; 
    // vector<vector<int>> adj = {{1, 2}, {3},{3, 4}, {5}, {5, 6}, {},{}}; 
    // vector<int> label = {7, 2, 6, 3, 8, 1, 4}; 
    // vector<int> minVertex(v, -1);  
    // vector<bool> visited(v, false);


    // int v = 6; 
    // vector<vector<int>> adj = {{1, 2}, {3, 4}, {4}, {5}, {}, {}}; 
    // vector<int> label = {9, 6, 4, 8, 2, 1}; 
    // vector<int> minVertex(v, -1);  
    // vector<bool> visited(v, false);




    for(int i=0;i<v;i++){
        if(!visited[i]){
            dfs(i,adj,label,minVertex,visited); //start dfs if node is not visited
        }
    }

    for(int i=0;i<v;i++){
        cout<<"Min Label for "<<i<<" : "<<minVertex[i]<<endl;
    }
    return 0;
}

void dfs(int u, vector<vector<int>>& adj, vector<int> &label, vector<int> &minVertex, vector<bool>& visited){
    visited[u]=true;
    minVertex[u]=u;

    for(int v: adj[u]){
        if(!visited[v]){
            dfs(v,adj,label,minVertex,visited);
        }
        if(label[minVertex[v]]<label[minVertex[u]]){  //after dfs we back track to the node to compare min vertex values
            minVertex[u]=minVertex[v];
        }
    }
}
