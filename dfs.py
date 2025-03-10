graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}
visitedNode = [] 


def dfs(visitedNode, graph, node):
    if node not in visitedNode:  # Check if node is already visited
        print(node, end=" ")  # Print the node
        visitedNode.append(node)  # Mark node as visited
        for neighbour in graph[node]:  # Iterate over adjacent nodes
            dfs(visitedNode, graph, neighbour)  # Recursively call DFS
            
            
Snode = input("Enter starting node (A, B, C, D, E): ").upper()


if Snode in graph:
    print("DFS Result:")
    dfs(visitedNode, graph, Snode)
else:
    print("Invalid starting node! Please enter a valid node (A, B, C, D, E).")