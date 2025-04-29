'''
There is a source (S) and destination (D) and a spacecraft has to go from S to D. There are N number of wormholes in
between which has following properties:

Each wormhole has an entry and an exit. Each wormhole is bi-directional i.e. one can enter and exit from
any of the ends. The time to cross the wormhole is given and the space craft may or may not use
the wormhole to reach D. The cost to travel outside wormhole between two points (x1, y1) and (x2, y2) is given by a
formula |x1 - x2| + |y1 - y2| where, (x1, y1) and (x2, y2) are the co-ordinates of two points. The co-ordinates of S
and D are given and we have to find the minimum cost to reach D from S. The main problem here is to ensure minimum cost
for the spaceship to go from source to destination co-ordinate using any number of warm-hole.
It is ok if you wont use any warmhole.

Note: It’s not mandatory to consider all the wormholes

First line contains t, number of test cases

Next line contains value of N. Next N lines contain the warmhole information.

each warmhole has 5 values. First 2 values are starting co-ordinate of warmhole and value no. 3 and 4 represents ending
co-ordinate of warmhole and 5th value represents cost to pass through this warmhole.

Constraints
1 < t < 10 1 < N < 6 -1 < x < 101 -1 < y < 101 0 < cost < 101

1
3
0 0 100 100
1 2 120 120 16
2 5 120 100 21
6 8 150 180 16

sample output
48
*/
'''


from itertools import permutations

#time is not needed for the answer, but the goal is to have the program process everything on less than 10 seconds
import time

'''
STEP FOR IMPLEMENTING djikstra algorithm
1. Define nodes (Source, Destinations, wormholes)
2. build edge between node, costs for wormholes, distance for anything else
3. initialize distance table
4. use min-heap queue and start the loop
5. check for every node, if it cost lower update
6. answer is final cost
'''

def dijikstra(x, y, current_cost, total_cost ):
    # global ans
    temp = [total_cost]
    # calculate distance between current x,y and destination and
    # choose the min value between total cost and current cost
    temp.append(current_cost + calcDistance((x,y), (destination[0], destination[1])))
    _res = min(temp)
    # print(ans)
    for i in range(T):
        if not visited[i]:
            visited[i] = True
            # recusively call for (exit x, exit y, cost for travel) with
            # {cost for travel = current cost + distance between (current x, current y) and (entry x, entry y) + wormhole cost})
            # for entry reverse between entry and exit
            temp.append(dijikstra(wormholes[i][2], wormholes[i][3], current_cost + calcDistance((x, y), (wormholes[i][0], wormholes[i][1])) + (wormholes[i][4]), _res))
            temp.append(dijikstra(wormholes[i][0], wormholes[i][1], current_cost + calcDistance((x, y), (wormholes[i][2], wormholes[i][3])) + (wormholes[i][4]), _res))
            visited[i] = False
    _res = min(temp)
    return _res

def calcDistance(point1, point2):
    res = abs(point2[0] - point1[0]) + abs(point2[1]-point1[1])
    # print(point1, point2, res, point2[0], point1[0], point2[1], point1[1])
    return res

if __name__ == '__main__':
    N = int(input())
    t0 = time.time()
    for n in range(N):
        source = ()
        destination = ()
        wormholes = []
        visited = [False] * 20
        T = 0
        T = int(input())
        source_x, source_y, dest_x, dest_y =  map(int, str(input()).split())
        source = (source_x, source_y)
        destination = (dest_x, dest_y)

        for i in range(T):
            x_entry , y_entry, x_exit, y_exit, cost  = map(int, str(input()).split())
            wormholes.append((x_entry, y_entry, x_exit, y_exit, cost))

        res = dijikstra(source[0], source[1], 0, float('inf'))
        print(f"#{n+1}", end=" ")
        print(res)

    t1 = time.time()
    print("process time: " + str(t1-t0))





'''
sample input and output
1
3
0 0 100 100
1 2 120 120 16
2 5 120 100 21
6 8 150 180 16

48

4
3
0 0 100 100
1 2 120 120 16
2 5 120 100 21
6 8 150 180 16
3
0 0 100 100
1 2 120 120 16
2 5 120 100 16
6 8 150 180 16
2
0 0 60 60
0 0 2 2 1
2 2 60 60 10
2
0 0 100 100
0 0 50 50 1
51 51 100 100 1

48
43
11
4

1
5
0 0 100 100
1 1 2 2 5
22 33 5 6 9
12 67 23 11 4
19 22 45 23 3
12 90 56 34 7

159

1
1
0 0 100 100
1 1 2 2 90

200

1
2
0 0 100 100
12 12 34 56 3
34 12 90 99 3

60
'''


