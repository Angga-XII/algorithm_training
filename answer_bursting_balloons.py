'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:

Input: nums = [1,5]
Output: 10


Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100


3 1 5 8
167

1 5
10

'''

#time is not needed for the answer, but the goal is to have the program process everything on less than 10 seconds
import time

'''
STEP FOR IMPLEMENTING DP 
1. Create a 2d array dp[left][right] representing the score between interval [left] and [right] 
2  calculate for every possible interval [left][right] from smalles to largest
3. use memoization to speedup calculations
4. add final balloon score
5. check final score on largest interval
'''

def maxCoins(nums):
    balloons = [1] + nums + [1]
    num_ballons =len(balloons)
    dp = [[0] * num_ballons for _ in range(num_ballons)]

    for interval in range(2,num_ballons):
        for i in range(num_ballons):
            if (i + interval >= num_ballons):
                continue
            _temp = []
            for k in range(i+1,i+interval):
                    value = dp[i][k] + balloons[i] * balloons[k] * balloons[i+interval] + dp[k][i+interval]
                    _temp.append(value)
                    # print(i, k, i + interval, value)
                    # print(_temp)
            dp[i][i + interval] = max(_temp) if _temp else 0
            # print(dp)
    res = dp[0][len(nums)+1]
    return res


if __name__ == '__main__':
    N = list(map(int, str(input()).split()))
    t0 = time.time()

    res = maxCoins(N)

    # print(f"#{n+1}", end=" ")
    print("res:", res)

    t1 = time.time()
    print("process time: " + str(t1-t0))
