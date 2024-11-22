#GRAPH TRAVERSAL ALGORITHMS
#Depth_first_search
def dfs_stack(graph,start):
    visited=set()#stores all visited nodes
    stack=[ start]#Initialises start node

    while stack:
        node=stack.pop()
        if node not in visited:
            print(node,end=" ")#end=" " is a way of formatting so that they are printed sideways
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
graph={
    "A":["S","D"], #S and D are neighbors of A in the graph
    "B":["S","D"],
    "C":["S","D"],
    "D":["A","B","C"],
    "S":["A","B","C"]
}
dfs_stack(graph,"S")

#Breadth_First search
from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    output=[]

    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node,end=" ")
            visited.add(node) 
            output.append(node)
            for neighbor in (graph[node]):
                if neighbor not in visited:
                    queue.append(neighbor)
    return output
graph={
    "A":["S","D"], #S and D are neighbors of A in the graph
    "B":["S","D"],
    "C":["S","D"],
    "D":["A","B","C"],
    "S":["A","B","C"]
}
bfs(graph,"S")