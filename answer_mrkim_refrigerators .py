#!/bin/python3


''' the probelem
Mr. Kim has to deliver refrigerators to N customers. From the office, he is going to visit all the customers and then return to his home.
Each location of the office, his home, and the customers is given in the form of integer coordinates (x,y) (0≤x≤100, 0≤y≤100) .
The distance between two arbitrary locations (x1, y1) and (x2, y2) is computed by |x1-x2| + |y1-y2|, where |x| denotes the absolute value
of x; for instance, |3|=|-3|=3. The locations of the office, his home, and the customers are all distinct. You should plan an optimal way
to visit all the N customers and return to his among all the possibilities.
You are given the locations of the office, Mr. Kim’s home, and the customers; the number of the customers is in the range of 5 to 10.
Write a program that, starting at the office, finds a (the) shortest path visiting all the customers and returning to his home.
Your program only have to report the distance of a (the) shortest path.

Constraints

5≤N≤10. Each location (x,y) is in a bounded grid, 0≤x≤100, 0≤y≤100, and x, y are integers.

Input

You are given 10 test cases. Each test case consists of two lines; the first line has N, the number of the customers, and the
following line enumerates the locations of the office, Mr. Kim’s home, and the customers in sequence. Each location consists of
the coordinates (x,y), which is reprensented by ‘x y’.

Output

Output the 10 answers in 10 lines. Each line outputs the distance of a (the) shortest path. Each line looks like ‘#x answer’
where x is the index of a test case. ‘#x’ and ‘answer’ are separated by a space.

I/O Example

Input (20 lines in total. In the first test case, the locations of the office and the home are (0, 0) and (100, 100) respectively,
and the locations of the customers are (70, 40), (30, 10), (10, 5), (90, 70), (50, 20).)

5 ← Starting test case #1

0 0 100 100 70 40 30 10 10 5 90 70 50 20

6 ← Starting test case #2

88 81 85 80 19 22 31 15 27 29 30 10 20 26 5 14

10 ← Starting test case #3

39 9 97 61 35 93 62 64 96 39 36 36 9 59 59 96 61 7 64 43 43 58 1 36

Output (10 lines in total)

#1 200

#2 304

#3 366
'''


from itertools import permutations

#time is not needed for the answer, but the goal is to have the program process everything on less than 10 seconds
import time

#matplotlib is not needed for the answer, i just wanted to visualize the points
import matplotlib.pyplot as plt

def plot(x, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, marker='o', color='blue', label='Path')  # Line with markers
    # Annotate each point with its coordinates
    idx = 0
    for x, y in zip(x, y):
        plt.text(x, y, f'({x},{y},{idx})', fontsize=12, ha='right', va='bottom', color='red')
        idx += 1
    # Formatting the plot
    plt.title('Line Plot with Coordinates')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()



#answer 366
# input = "39 9 97 61 35 93 62 64 96 39 36 36 9 59 59 96 61 7 64 43 43 58 1 36"
#answer 100
# input = "0 0 0 100 0 50 0 25 0 10"
#answer 200
# input = "0 0 100 100 70 40 30 10 10 5 90 70 50 20"
#answer 304
# input = "88 81 85 80 19 22 31 15 27 29 30 10 20 26 5 14"
#answer
# input = "10 0 5 0 0 50 5 25 0 0"
#answer 370
# input = "39 9 61 15 35 93 62 64 96 39 36 36 9 59 59 96 61 7 64 43 43 58 1 36"



def calcDistance(p0, p1):
    # print(x1, x2, y1, y2)
    return abs(p0[0]-p1[0]) + abs(p0[1]-p1[1])

def firstStep(point, pickup_points):
    distance = []
    for points in pickup_points:
        distance.append(calcDistance(point,points))
    # print(distance)
    return distance.index(min(distance))

def pathFinding(office, home, pickup_points):
    #removed 1 point to reduce the permutation total possibilities from a maximum of 10! to 9!
    removed_id = firstStep(home, pickup_points)
    removed_point = pickup_points[removed_id]
    pickup_points.pop(removed_id)

    min_distance = float('inf')
    best_path = None

    #calculate the distances for all possible permutations
    for perm in permutations(pickup_points):
        # path = [removed_point] + list(perm)
        path = [office] + list(perm) + [removed_point]
        distance = sum(calcDistance(path[i], path[i + 1]) for i in range(len(path) - 1))

        if distance < min_distance:
            min_distance = distance
            best_path = path
    # print(best_path + [home])
    min_distance += calcDistance(home, best_path[-1])
    return min_distance

#same function but without the optimization
# def pathFinding(office, home, pickup_points):
#
#     min_distance = float('inf')
#     best_path = None
#     for perm in permutations(pickup_points):
#         path = [office] + list(perm) + [home]
#         distance = sum(calcDistance(path[i], path[i + 1]) for i in range(len(path) - 1))
#
#         if distance < min_distance:
#             min_distance = distance
#             best_path = path
#     print(best_path)
#     return min_distance


if __name__ == '__main__':
    t0 = time.time()
    N = 10
    for i in range(N):
        #input should've been inputted from console using input(), this is to make testing faster
        coords = list(map(int, str(input()).split()))

        # Extract coordinates
        office = (coords[0], coords[1])
        home = (coords[2], coords[3])
        pickup_points = [(coords[i], coords[i + 1]) for i in range(4, len(coords), 2)]

        res = pathFinding(office, home, pickup_points)
        print(f"#{i+1}", end=" ")
        print(res)

        #plot the points for easier debugging and visualization not needed in the answer
        # x = coords[::2]
        # y = coords[1::2]
        # plot(x,y)

    t1 = time.time()
    print("process time: " + str(t1-t0))