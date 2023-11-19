from collections import deque

def getMinimumMoves(maze, k):
    n, m = len(maze), len(maze[0])  # Dimensions of the maze
    target = (n - 1, m - 1)  # The destination cell
    visited = set()  # Set to keep track of visited cells
    queue = deque([(0, 0, 0)])  # Queue for BFS: (x, y, moves)

    # Check if the next cell is valid and has no obstacles
    def is_valid(nx, ny, x, y):
        if 0 <= nx < n and 0 <= ny < m:  # Check boundaries
            if maze[nx][ny] == 1:  # Check for obstacle
                return False
            if x == nx:  # Horizontal move
                for j in range(min(y, ny) + 1, max(y, ny)):
                    if maze[x][j] == 1:
                        return False
            elif y == ny:  # Vertical move
                for i in range(min(x, nx) + 1, max(x, nx)):
                    if maze[i][y] == 1:
                        return False
            return True
        return False

    # Perform BFS
    while queue:
        x, y, moves = queue.popleft()
        if (x, y) == target:
            return moves
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(k, 0), (-k, 0), (0, k), (0, -k)]:  # Possible moves
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, x, y) and (nx, ny) not in visited:
                queue.append((nx, ny, moves + 1))
    return -1  # If the destination is not reachable

# Example usage
maze = [[0, 0, 0], [1, 0, 0]]
k = 2
print(getMinimumMoves(maze, k))
