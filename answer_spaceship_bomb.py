'''
You’ll be given a grid as below:

    0 1 0 2 0
    0 2 2 2 1
    0 2 1 1 1
    1 0 1 0 0
    0 0 1 2 2
    1 1 0 0 1
    x x S x x

In the grid above,
  1: This cell has a coin.
  2: This cell has an enemy.
  0: It contains nothing.

  The highlighted(yellow) zone is the control zone. S is a spaceship that we need to control so that we can get
  maximum coins.
  Now, S’s initial position will be at the center and we can only move it right or left by one cell or do not move.
  At each time, the non-highlighted part of the grid will move down by one unit.
  We can also use a bomb but only once. If we use that, all the enemies in the 5×5 region above the control zone
  will be killed.
  If we use a bomb at the very beginning, the grid will look like this:

    0 1 0 2 0
    0 0 0 0 1
    0 0 1 1 1
    1 0 1 0 0
    0 0 1 0 0
    1 1 0 0 1
    x x S x x

  As soon as, the spaceship encounters an enemy or the entire grid has come down, the game ends.
  For example,
  At the very first instance, if we want to collect a coin we should move left( coins=1). This is because when the
  grid comes down by 1 unit we have a coin on the second position and by moving left we can collect that coin.
  Next, we should move right to collect another coin (coins=2).
  After this, remain at the same position (coins=4).
  This is the current situation after collecting 4 coins.

    0 1 0 2 0
    0 1 0 0 0
    0 2 2 2 1 -->after using 0 0 0 0 1
    x x S x x -->bomb x x S x x

   Now, we can use the bomb to get out of this situation. After this, we can collect at most 1 coin. So maximum coins=5.

'''


import time

def bombed(grid):
    new_grid = grid[:-5]
    for row in grid[-5:]:
        new_grid.append(row.replace('2','0'))
    return new_grid
def spaceship(grid, pos, isBombed, total_coins, path):
    res = 0
    if grid:
        # print("test", grid, pos, isBombed, total_coins)
        if grid[-1][pos] == '1': total_coins += 1
        # elif grid[-1][pos] == '2': return 0
        _temp = [total_coins]
        res = max(_temp)
        if not isBombed:
            coins_bomb = spaceship(bombed(grid), pos, True, res, path+" b")
            _temp.append(coins_bomb)
        if pos > 0:
            coins_left = spaceship(grid[0:-1],  pos-1, isBombed, res,  path+" l")
            _temp.append(coins_left)
        if pos < 4:
            coins_right = spaceship(grid[0:-1], pos+1, isBombed, res,  path+" r")
            _temp.append(coins_right)

        coins_stay = spaceship(grid[0:-1], pos, isBombed, res,  path+" s")
        _temp.append(coins_stay)
        # print(_temp, isBombed, pos, total_coins, len(grid))
        res = max(_temp)
        # print("path: ", path, res)
    return res
# start l r s s lb s s r s r r s
if __name__ == '__main__':
    N = int(input())
    t0 = time.time()
    grid = []
    for n in range(N):
        # grid.append(list(map(int, str(input()).split())))
        grid.append(str(input().replace(' ','')))
    #check if start on pipes
    res = 0
    res = spaceship(grid, 2, False, 0, "start")
    print(f"#{n+1}", end=" ")
    print(res)
    t1 = time.time()
    print("process time: " + str(t1-t0))


'''
1
12
0 1 0 2 0
0 2 2 2 1
0 2 1 1 1
1 0 1 0 0
0 0 1 2 2
1 1 0 0 1
0 1 0 2 0
0 2 2 2 1
0 2 1 1 1
1 0 1 0 0
0 0 1 2 2
1 1 0 0 1
x x S x x


1
12
0 1 0 2 0
0 2 2 2 1
0 2 1 1 1
2 2 2 2 2
0 0 1 2 2
1 1 0 0 1
0 1 0 2 0
0 2 2 2 1
0 2 1 1 1
1 0 1 0 0
0 0 1 2 2
1 1 0 0 1
x x S x x
'''