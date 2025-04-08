#!/bin/python3


''' the probelem
Byteland has n cities and m flight connections. Your task is to design a round trip that begins in a city, goes through
one or more other cities, and finally returns to the starting city. Every intermediate city on the route has to be distinct.

Input
The first input line has two integers n and m: the number of cities and flights. The cities are numbered 1,2,\dots,n.
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


def pathFinding():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    visited = [0] * (n + 1)  # 0 = unvisited, 1 = visiting, 2 = visited
    parent = [-1] * (n + 1)
    cycle = []

    def dfs(u):
        global cycle
        visited[u] = 1  # Mark as visiting
        for v in graph[u]:
            if visited[v] == 0:
                parent[v] = u
                if dfs(v):
                    return True
            elif visited[v] == 1:
                # Cycle found
                cycle_start = v
                cycle_end = u
                cycle = [cycle_start]
                while cycle_end != cycle_start:
                    cycle.append(cycle_end)
                    cycle_end = parent[cycle_end]
                cycle.append(cycle_start)
                cycle.reverse()
                return True
        visited[u] = 2  # Mark as fully visited
        return False

    found = False
    for i in range(1, n + 1):
        if visited[i] == 0:
            if dfs(i):
                found = True
                break

    if found:
        print(len(cycle))
        print(' '.join(map(str, cycle)))
    else:
        print("IMPOSSIBLE")



if __name__ == '__main__':
    t0 = time.time()
    pathFinding()
    # N = 10
    # for i in range(N):
    #     #input should've been inputted from console using input(), this is to make testing faster
    #     coords = list(map(int, str(input()).split()))
    #
    #     # Extract coordinates
    #     office = (coords[0], coords[1])
    #     home = (coords[2], coords[3])
    #     pickup_points = [(coords[i], coords[i + 1]) for i in range(4, len(coords), 2)]
    #
    #     res = pathFinding(office, home, pickup_points)
    #     print(f"#{i+1}", end=" ")
    #     print(res)
    #
    #     #plot the points for easier debugging and visualization not needed in the answer
    #     # x = coords[::2]
    #     # y = coords[1::2]
    #     # plot(x,y)

    t1 = time.time()
    print("process time: " + str(t1-t0))