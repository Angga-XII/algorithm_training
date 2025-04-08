#!/bin/python3


''' the probelem
Byteland has n cities and m flight connections. Your task is to design a round trip that begins in a city, goes through
one or more other cities, and finally returns to the starting city. Every intermediate city on the route has to be distinct.

Input
The first input line has two integers n and m: the number of cities and flights. The cities are numbered 1,2,...,n.
Then, there are m lines describing the flights. Each line has two integers a and b: there is a flight connection from city a to city b. All connections are one-way flights from a city to another city.

Output
First print an integer k: the number of cities on the route. Then print k cities in the order they will be visited. You can print any valid solution.
If there are no solutions, print "IMPOSSIBLE".

Constraints

1 < n < 10^5
1 < m < 2 x 10^5
1 < a,b < n

Example
Input:

4 5
1 3
2 1
2 4
3 2
3 4

Output:

4
2 1 3 2

'''


from itertools import permutations

#time is not needed for the answer, but the goal is to have the program process everything on less than 10 seconds
import time


'''
Step 1: Model the Graph
Represent cities as nodes and flights as directed edges.
Build an adjacency list from the input to represent the graph.

Step 2: Initialize Tracking Structures
visited[]: tracks state of each node. 0 = not visited, 1 = visiting ,2 = visited
parent[]: to trace the path and reconstruct the cycle.
cycle[]: will store the final cycle when found.

Step 3: Run DFS from Each Unvisited Node
For every unvisited node, start a DFS.
Mark it as visiting (1).

Step 4: During DFS, Look for Back Edges
For each neighbor:
If it's unvisited, recursively continue DFS.
If it's already marked visiting, it means a cycle is detected (back edge to an ancestor).
Use the parent array to reconstruct the path (cycle) from the current node back to the start of the cycle.

Step 5: Reconstruct the Cycle
Start from the current node and trace back using parent[] until you reach the repeated node.
Append all nodes in this trace to the cycle list.
Reverse the list to get the correct cycle order.

'''

def DFS(city):
    global cycle
    visited[city] = True
    # print("test cycle", cycle, city)
    for i in graph[city]:
        if cycle:
            break
        if not visited[i]:
            parent[i] = city
            DFS(i)
        elif visited[i]:
            start = i
            end = city
            cycle = [start]
            # print("test start", start, end, cycle)
            # print(parent)
            while end != start:
                cycle.append(end)
                end = parent[end]
                if (end == -1):
                    cycle = []
                    # print("test 2", cycle)
                    break
                # print("test 1", cycle)

            if cycle:
                cycle.append(start)
                cycle.reverse()



global graph
global visited
global parent
# global cycle

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    visited = [False] * (n)
    parent = [-1] * (n)
    cycle = []

    t0 = time.time()

    for i in range(m):
        start_city, end_city = map(int, input().split())
        graph[start_city].append(end_city)
    # print(graph)
    for city in range(0, n):
        if not visited[city]:
            DFS(city)

    if cycle:
        print(len(cycle))
        print(' '.join(map(str, cycle)))
    else:
        print("IMPOSSIBLE")

    t1 = time.time()
    print("process time: " + str(t1-t0))