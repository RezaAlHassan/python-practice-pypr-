#Reza Al Hassan - 1910876

#The find_shortest_path() function takes four arguments: grid (a 2D list representing the grid), source_cell (a tuple containing the row and column indices of the source cell), goal_cells (a list of tuples containing the row and column indices of the goal cells), and blocked_cells (a list of tuples containing the row and column indices of the blocked cells).
#First, the function creates a visited matrix to keep track of the cells that have been visited during the traversal. It also creates a queue data structure and initializes it with the source cell and a distance of 0. The BFS traversal then begins with a while loop that continues as long as the queue is not empty.
#Inside the loop, the function dequeues the next cell from the queue, checks if it is a goal cell (by comparing it with the elements of the goal_cells list), and if so, returns the distance to that cell.
#If the dequeued cell is not a goal cell, the function checks its neighbors (i.e., cells that are one unit up, down, left, or right from it) to see if they are valid (i.e., within the grid boundaries and not blocked) and have not been visited yet. For each valid neighbor, the function marks it as visited, adds it to the queue, and sets its distance to the current cell's distance plus 1.
#the function continues the BFS traversal until either a goal cell is found (and its distance is returned) or the queue becomes empty (which means that there is no path from the source cell to any goal cell).

from collections import deque

# function to check if a cell is valid and not blocked
def is_valid_cell(row, col, num_rows, num_cols, blocked_cells):
    if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
        return False
    if (row, col) in blocked_cells:
        return False
    return True

# function to find the shortest path to the closest goal cell
def find_shortest_path(grid, source_cell, goal_cells, blocked_cells):
    num_rows, num_cols = len(grid), len(grid[0])
    visited = [[False]*num_cols for _ in range(num_rows)]
    queue = deque([(source_cell, 0)])
    visited[source_cell[0]][source_cell[1]] = True
    while queue:
        current_cell, distance = queue.popleft()
        if current_cell in goal_cells:
            return distance
        for row_offset, col_offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            next_row, next_col = current_cell[0] + row_offset, current_cell[1] + col_offset
            if is_valid_cell(next_row, next_col, num_rows, num_cols, blocked_cells) and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                queue.append(((next_row, next_col), distance+1))
    return -1  # no path found

# sample input
num_rows, num_cols = 5, 6
source_cell = (3, 1)
goal_cells = [(2, 6), (4, 3), (6, 5)]
blocked_cells = [(0, 3), (1, 1), (1, 5), (3, 3), (3, 4), (4, 1)]

# create grid with blocked cells marked as 'X'
grid = [['.' for _ in range(num_cols)] for _ in range(num_rows)]
for cell in blocked_cells:
    grid[cell[0]][cell[1]] = 'X'
for goal_cell in goal_cells:
    grid[goal_cell[0]][goal_cell[1]] = 'G'
grid[source_cell[0]][source_cell[1]] = 'S'

# print input grid
print("Input grid:")
for row in grid:
    print("".join(row))

# find shortest path and print result
shortest_path = find_shortest_path(grid, source_cell, goal_cells, blocked_cells)
if shortest_path >= 0:
    print(f"\nShortest path to closest goal cell: {shortest_path}")
else:
    print("\nNo path found to any goal cell.")

