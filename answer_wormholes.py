'''
There is a source (S) and destination (D) and a spacecraft has to go from S to D. There are N number of wormholes in between which has following properties:

Each wormhole has an entry and an exit. Each wormhole is bi-directional i.e. one can enter and exit from any of the ends. The time to cross the wormhole is given and the space craft may or may not use the wormhole to reach D. The cost to travel outside wormhole between two points (x1, y1) and (x2, y2) is given by a formula |x1 - x2| + |y1 - y2|

where, (x1, y1) and (x2, y2) are the co-ordinates of two points. The co-ordinates of S and D are given and we have to find the minimum cost to reach D from S. The main problem here is to minimum cost to reach spaceship from source to destination co-ordinate using any number of warm-hole. It is ok if you wont use any warmhole.

Note: It’s not mandatory to consider all the wormholes
First line contains t, number of test cases

There are N number of warmholes each warmhole has 5 values. First 2 values are starting co-ordinate of warmhole and after that value no. 3 and 4 represents ending co-ordinate of warmhole and last 5th value is represents cost to pass through this warmhole.

Line 1 contains value of N. Line 2 Conatins Source and Destination coordinate. Next N lines contain the warmhole information.

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
1. create a class to define the graph structure indluding each node (S,D Wormholes) with their attached weights (Distances or cost)
2. build the graph using information from the input
3. implement djikstra and calculate each node distance to each other updating the smallest one
'''
def pathFinding(airfares, T):
    # implement BitMask DP
    INF = float('inf')
    bitmask = [[INF] * T for _ in range(1 << T)]
    bitmask[1][0] = 0  # Start from office 0 with only office 0 visited
    # print(dp)
    for mask in range(1<<T):

        for i in range(T):
            if bitmask[mask][i] == INF:
                continue
            for j in range(T):
                if ((mask & (1 << j)) == 0 and airfares[i][j] != 0):
                    new_mask = mask | (1 << j)
                    bitmask[new_mask][j] = min(bitmask[new_mask][j], bitmask[mask][i] +  airfares[i][j])
    res = INF
    for id in range(T):
        final = bitmask[-1][id] + airfares[id][0]
        res = final if(final < res) else res
    # min_distance += calcDistance(home, best_path[-1])
    return res


if __name__ == '__main__':
    N = int(input())
    t0 = time.time()
    for n in range(N):
        T = int(input())
        coords =  list(map(int, str(input()).split()))
        start = (coords[0], coords[1])
        destination = (coords[2], coords[3])
        wormholes = []
        for i in range(T):
            _temp = list(map(int, str(input()).split()))
            for j in range(len(_temp)):
                _temp[j] = float('inf') if (_temp[j] == 0 and i != j) else _temp[j]
            wormholes.append(_temp)


        res = pathFinding(wormholes, T)
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