'''
Mr. Lee has to travel various offices abroad to assist branches of each place. But he has a problem.
The airfare would be real high as all offices he has to visit are in foreign countries. He wants to visit every
location only one time and return home with the lowest expense. Help this company-caring man calculate the lowest expense.


Input format
Several test cases can be included in the inputs. T, the number of cases is given in the first row of the inputs.
After that, the test cases as many as T (T ≤ 30) are given in a row. N, the number of offices to visit is given on
the first row per each test case. At this moment, No. 1 office is regarded as his company (Departure point).
(1 ≤ N ≤ 12) Airfares are given to move cities in which branches are located from the second row to N number rows.
i.e. jth number of ith row is the airfare to move from ith city to jth city. If it is impossible to move between
two cities, it is given as zero.

Output format
Output the minimum airfare used to depart from his company, visit all offices, and then return his company on the
first row per each test case.

Example of Input
1
5
9 9 2 9 5
6 3 5 1 5
1 8 3 3 3
6 0 9 6 8
6 6 9 4 8

1
5
0 14 4 10 20
14 0 7 8 7
4 5 0 7 16
11 7 9 0 2
18 7 17 4 0

1
12
0 14 4 10 20 14 0 7 8 7 8 7
14 0 7 8 7 4 5 0 7 16 7 16
4 5 0 7 16 11 7 9 0 2 0 2
11 7 9 0 2 18 7 17 4 0 4 0
18 7 17 4 0 0 14 4 10 20 10 20
0 14 4 10 20 14 0 7 8 7 8 7
14 0 7 8 7 4 5 0 7 16 7 16
4 5 0 7 16 11 7 9 0 2 0 2
11 7 9 0 2 18 7 17 4 0 4 0
18 7 17 4 0 0 14 4 10 20 10 20
11 7 9 0 2 18 7 17 4 0 4 0
18 7 17 4 0 0 14 4 10 20 10 20
answer 51

3
5
0 14 4 10 20
14 0 7 8 7
4 5 0 7 16
11 7 9 0 2
18 7 17 4 0
5
9 9 2 9 5
6 3 5 1 5
1 8 3 3 3
6 0 9 6 8
6 6 9 4 8
3
0 2 24
3 0 2
0 4 0
12
0 14 4 10 20 14 0 7 8 7 8 7
14 0 7 8 7 4 5 0 7 16 7 16
4 5 0 7 16 11 7 9 0 2 0 2
11 7 9 0 2 18 7 17 4 0 4 0
18 7 17 4 0 0 14 4 10 20 10 20
0 14 4 10 20 14 0 7 8 7 8 7
14 0 7 8 7 4 5 0 7 16 7 16
4 5 0 7 16 11 7 9 0 2 0 2
11 7 9 0 2 18 7 17 4 0 4 0
18 7 17 4 0 0 14 4 10 20 10 20
11 7 9 0 2 18 7 17 4 0 4 0
18 7 17 4 0 0 14 4 10 20 10 20

Example of Output

30
18
CUSTOM - 31 <- 4
*/
'''


from itertools import permutations

#time is not needed for the answer, but the goal is to have the program process everything on less than 10 seconds
import time


'''
STEP FOR IMPLEMENTING DP
1. define dp bitmask[mask][N] array, with mask = visited city in bit form, N number of city
2. define the first step bitmask[1][0] as visited with value 0
3. loop for every mask
4. loop for every city checking for valid value
5. loop for every city that is unvisited
5. update mask and bitmask[mask][n] value
6. check minimal value on bitmask[final_mask]
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


# def pathFinding(wormholes, city):
#     min_fare = float('inf')
#     best_path = None
#     print(len(list(permutations(range(city)[1:]))))
#     #calculate the distances for all possible permutations
#     for perm in permutations(range(city)[1:]):
#         # print(1)
#         path = [0] + list(perm) + [0]
#         total_fares = 0
#         for i in range(len(path) - 1):
#             # print(wormholes[path[i]][path[i + 1 % len(path) - 1]])
#             total_fares += wormholes[path[i]][path[i + 1 % (len(path) - 1)]]
#         # total_fares = sum(wormholes[path[i]][path[i+1 % len(path)-1]] for i in range(len(path) - 1))
#
#         if total_fares < min_fare:
#             print(total_fares)
#             min_fare = total_fares
#             best_path = path
#
#     print(best_path, min_fare)
#     # min_distance += calcDistance(home, best_path[-1])
#     return min_fare


if __name__ == '__main__':
    N = int(input())
    t0 = time.time()
    for n in range(N):
        T = int(input())
        airfares = []
        for i in range(T):
            _temp = list(map(int, str(input()).split()))
            for j in range(len(_temp)):
                _temp[j] = float('inf') if (_temp[j] == 0 and i != j) else _temp[j]
            airfares.append(_temp)


        res = pathFinding(airfares, T)
        print(f"#{n+1}", end=" ")
        print(res)

    t1 = time.time()
    print("process time: " + str(t1-t0))
