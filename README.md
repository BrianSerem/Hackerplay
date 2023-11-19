Maze in HackerPlay

HackerMan is in a maze at HackerPlay, where children play for recreation. The maze is an
�
×
�
n×m grid of cells, and each cell is either empty (denoted by 0) or contains an obstacle (denoted by 1). HackerMan starts at the top-left cell (0, 0) and wants to reach the bottom-right cell (n - 1, m - 1).

HackerMan can jump a certain number of cells (denoted by k) in one move, either horizontally or vertically, but cannot jump over an obstacle. Specifically, HackerMan can move:

From (i, j) to (i + x, j), where
1
≤
�
≤
�
1≤x≤k, if the destination cell is in the maze and there are no obstacles in the horizontal path to the destination cell.
From (i, j) to (i, j + x), where
1
≤
�
≤
�
1≤x≤k, if the destination cell is in the maze and there are no obstacles in the vertical path to the destination cell.
From (i, j) to (i - x, j), where
1
≤
�
≤
�
1≤x≤k, if the destination cell is in the maze and there are no obstacles in the horizontal path to the destination cell.
From (i, j) to (i, j - x), where
1
≤
�
≤
�
1≤x≤k, if the destination cell is in the maze and there are no obstacles in the vertical path to the destination cell.
The challenge is to write a function getMinimumMoves(maze, k) that finds the minimum number of moves in which HackerMan can reach the destination cell. If it is impossible to reach the destination cell, the function should return -1.