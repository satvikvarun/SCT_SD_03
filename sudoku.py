# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(row)

# Function to check if it's safe to place a number at grid[row][col]
def is_safe(grid, row, col, num):
    # Check the row
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    # Check the column
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    # Check the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    
    return True

# Function to solve the Sudoku grid using backtracking
def solve_sudoku(grid):
    # Find the first empty cell
    empty_cell = find_empty_location(grid)
    if not empty_cell:
        return True  # No more empty cells, puzzle is solved
    
    row, col = empty_cell
    
    # Try all numbers from 1 to 9 in this cell
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num  # Make tentative assignment
            
            # Recur to solve the rest of the grid
            if solve_sudoku(grid):
                return True
            
            # Undo assignment (backtrack)
            grid[row][col] = 0
    
    return False  # Trigger backtracking

# Function to find an empty cell (marked by 0)
def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # Return row, column of empty cell
    return None  # No empty cells found

# Example Sudoku puzzle (0s represent empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_grid):
    print("Sudoku solved successfully!")
    print_grid(sudoku_grid)
else:
    print("No solution exists!")
