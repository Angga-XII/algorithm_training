''' the problem
Samsung wants to explore some of the rare elements for its semiconductor manufacturing. Scientists use one vehicle to
explore the region in order to find the rare elements. The vehicle can move only in explored region where roads have
already been constructed. The vehicle cannot move on unexplored region where roads are not there. In the current
situation, rare elements are present in explored region only. Unexplored regions do not contain any rare elements.

The shortest path for vehicle to a rare element position is called Moving Path. The longest of the paths to all rare
elements from a region called Longest Distance.

Scientists need to construct one research center so that the research center will be at the position where the
longest path to the rare elements will be shortest. This is called Shortest Longest Distance.

Constraint

The region provided will be square region i.e. NxN (where 5 <= N <= 20).
There can be minimum of 2 rare elements and maximum of 4 rare elements, i.e. 2 <= C <= 4.
Roads are represented by 1 while no road area is represented by 0.
Vehicle can move only on roads in explored area.
The rare elements will only be present where road are there. Rare elements will not be present where roads are not present.
Vehicle can move in UP, DOWN, LEFT and RIGHT directions.
The starting index for rare element is considers as 1.

Input:

First line will be the number of test cases. Second line will indicate region area (N) and number of rare elements (C).
Next C lines will contain the position of rare elements. After that N lines will provide the region details where to
tell where roads are present and where roads are not present.

Output:

Output #testcase followed by space and then shortest longest distance.


Input -
6
5 2
4 3
3 4
1 1 0 0 0
1 1 0 0 0
1 1 1 1 1
1 1 1 0 1
1 1 1 1 1
8 2
5 6
6 4
1 1 1 1 1 1 0 0
1 1 1 1 1 1 1 0
1 1 0 1 0 1 1 0
1 1 1 1 0 1 1 0
1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
10 3
8 2
5 3
7 1
0 0 0 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1 1 0
1 0 0 1 0 0 0 0 1 0
1 1 1 1 1 1 1 1 1 1
1 1 1 1 0 1 0 0 1 1
1 1 1 1 0 1 0 0 1 1
1 1 1 1 0 1 0 0 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 0 0 1 0 0 1 1
1 1 1 1 1 1 1 1 1 1
15 4
11 15
15 9
1 2
14 3
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 0 1 1 1 1 1 1 1 1 1 1 1 0 1
1 0 1 0 0 0 1 0 0 0 0 1 1 0 1
1 0 1 0 0 0 1 0 0 0 0 1 1 0 1
1 0 1 1 1 1 1 1 1 1 1 1 1 1 1
1 0 1 0 0 0 1 0 0 0 0 1 1 0 1
1 0 1 0 0 0 1 1 1 1 1 1 1 1 1
1 0 1 0 0 0 1 0 0 0 0 1 1 0 1
1 0 1 0 0 0 1 0 0 0 0 1 1 0 1
1 0 1 0 0 0 1 0 0 0 0 1 1 0 1
1 0 1 0 0 0 1 0 0 0 0 1 1 0 1
1 0 1 0 0 0 1 0 0 0 0 1 1 0 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 1 0 0 0 1 1 1 1 1 1 1 0 1
0 0 1 1 1 1 1 1 1 1 1 1 1 1 1
20 4
13 6
20 4
1 2
17 16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0
1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
1 0 1 0 0 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0
1 0 1 0 0 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 0 1 0 0 0 0 0 0 0 1 0 0 1 1 1 0 0 1 1
1 0 1 0 0 0 0 0 0 0 1 0 0 1 1 1 0 0 1 1
1 0 1 0 0 0 0 0 0 0 1 0 0 1 1 1 0 0 1 1
1 0 1 0 0 0 0 0 0 0 1 0 0 1 1 1 0 0 1 1
1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1
1 0 1 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 1 1
1 0 1 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 1 1
1 0 1 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 1 1
1 0 1 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
5 2
2 1
3 5
1 0 1 1 1
1 1 1 0 1
0 1 1 0 1
0 1 0 1 1
1 1 1 0 1

Output -
1
2
2
12
15
4
'''


'''
STEP FOR IMPLEMENTING BFS
1. Create a queue
2. track visited cell
3. start exploring from the given position
4. check for valid connection
5. count visited position
'''

from itertools import permutations

#time is not needed for the answer, but the goal is to have the program process everything on less than 10 seconds
import time

def checkConnectedRoads(grid, x, y):
    res = []
    grid_size = len(grid)

    #check top
    if (x>0):
        candidate = grid[x-1][y]
        if(candidate == 1):
            res.append((x-1,y))

    #check bottom
    if (x<grid_size-1):
        candidate = grid[x+1][y]
        if(candidate == 1):
            res.append((x+1,y))

    #check left
    if (y>0):
        candidate = grid[x][y-1]
        if(candidate == 1):
            res.append((x,y-1))

    #check left
    if (y<grid_size-1):
        candidate = grid[x][y+1]
        if(candidate == 1):
            res.append((x,y+1))

    return res

def pathFinding(grid, targets):
    grid_size = len(grid)
    target_size = len(targets)
    res = float('inf')
    traversal = []

    from collections import deque

    for target in targets:
        res = float('inf')
        q = deque()
        visited = []
        distances = []

        for i in range(grid_size):
            visited.append([False] * grid_size)
            distances.append([0] * grid_size)

        visited[target[0]][target[1]] = True
        q.append((target[0], target[1]))

        while q:
            current = q.popleft()

            connected_road = checkConnectedRoads(grid, current[0], current[1])
            for connection in connected_road:
                if not(visited[connection[0]][connection[1]]):
                    q.append(connection)
                    visited[connection[0]][connection[1]] = True
                    distances[connection[0]][connection[1]] = 1 + distances[current[0]][current[1]]
        traversal.append(distances)

    final = []

    for i in range(grid_size):
        final.append([0] * grid_size)

    for x in range(grid_size):
        for y in range(grid_size):
                final[x][y] = [traversal[i][x][y] for i in range(target_size)]

    # print(traversal)
    # print(final[x][y])

    # print("targets", targets)
    for x in range(grid_size):
        for y in range(grid_size):
            value = max(final[x][y])
            if min(final[x][y]) != 0 and value < res:
                res = value

    return res

if __name__ == '__main__':
    N = int(input())
    t0 = time.time()
    for i in range(N):
        target = []
        grid = []
        matrix_size, n = map(int, str(input()).split())
        for _ in range(n):
            x, y = map(int, str(input()).split())
            target.append((x-1,y-1))
        for _ in range(matrix_size):
            _temp = list(map(int, str(input()).split()))
            grid.append(_temp)

        res = pathFinding(grid, target)

        print(f"#{i+1}", end=" ")
        print(res)

    t1 = time.time()
    print("process time: " + str(t1-t0))