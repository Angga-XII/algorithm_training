from functools import lru_cache

def solve(grid, start_col):
    """
    Solve for maximum score and path on the scrolling grid with one bomb using recursion with memoization.

    grid: list of lists of ints (0,1,2) for rows 0..n-1 (bottommost row is grid[-1], i.e., first encountered)
    start_col: int, starting column index
    Returns: (max_score: int, path: list of actions)
    Actions: 'left', 'stay', 'right', 'bomb'
    """
    rows = len(grid)
    cols = len(grid[0])

    @lru_cache(None)
    def dfs(row, col, bomb_used, bomb_effect):
        # Base: reached above top
        if row < 0:
            return 0, []

        best_score = -float('inf')
        best_path = []

        # Option 1: use bomb (if not used yet)
        if not bomb_used:
            # Bomb sets effect for this turn
            cur_effect = 5
            # Landing at same column
            cell = grid[row][col]
            # Check safety
            if cell != 2 or cur_effect > 0:
                # Score gained
                gain = 1 if cell == 1 else 0
                # Decrease effect for next step
                next_effect = cur_effect - 1
                score, path = dfs(row - 1, col, True, next_effect)
                total = gain + score
                if total > best_score:
                    best_score = total
                    best_path = ['bomb'] + path

        # Option 2: normal moves
        for move, action in [(-1, 'left'), (0, 'stay'), (1, 'right')]:
            new_col = col + move
            if 0 <= new_col < cols:
                cur_effect = bomb_effect
                cell = grid[row][new_col]
                # If encounter enemy without effect, skip
                if cell == 2 and cur_effect == 0:
                    continue
                # Gain
                gain = 1 if cell == 1 else 0
                # Next effect
                next_effect = max(cur_effect - 1, 0)
                score, path = dfs(row - 1, new_col, bomb_used, next_effect)
                total = gain + score
                if total > best_score:
                    best_score = total
                    best_path = [action] + path

        return best_score, best_path

    # Start recursion from the bottommost row (index rows-1)
    max_score, path = dfs(rows - 1, start_col, False, 0)
    return max_score, path

import time
def main():
    # Read grid input row by row
    m = int(input("Enter number of rows (including start row): "))
    t0 = time.time()
    grid = []
    start_col = None
    for i in range(m):
        tokens = input(f"Row {i}: ").split()
        row_vals = []
        for j, tok in enumerate(tokens):
            if tok.upper() == 'S':
                start_col = j
                row_vals.append(0)
            else:
                row_vals.append(int(tok))
        grid.append(row_vals)

    if start_col is None:
        print("Error: Start position 'S' not found in input.")
        return

    # Remove the start row; process only the rows above start
    grid_above = grid[:-1]
    score, path = solve(grid_above, start_col)

    print(f"Maximum score: {score}")
    t1 = time.time()
    print("process time: " + str(t1-t0))
    # print("Moves:")
    # for step, action in enumerate(path, 1):
    #     print(f"Turn {step}: {action}")

if __name__ == '__main__':
    main()
