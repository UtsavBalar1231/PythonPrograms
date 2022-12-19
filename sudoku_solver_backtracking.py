import math

# Open the file and read the sudoku grid
sudoku = open("sudoku9TB.txt", "r")
sudoku = sudoku.read().splitlines()

# Pop the first line of the file which is the size of the grid
sudoku_size = sudoku.pop(0)
# Convert the size to an integer
sudoku_size = int(sudoku_size)

# Trim the grid to the size of the grid
sudoku = [x.strip() for x in sudoku]

# Split the grid into a list of lists
sudoku = [x.split() for x in sudoku]

# Convert the grid to integers
sudoku = [[int(y) for y in x] for x in sudoku]

# print the grid
# print(sudoku)


def is_valid(sudoku, row, col, num):
    # Check if the number is in the row
    if num in sudoku[row]:
        return False

    # Check if the number is in the column
    for i in range(sudoku_size):
        if sudoku[i][col] == num:
            return False

    # Check if the number is in the box
    box_size = int(math.sqrt(sudoku_size))
    box_row = row // box_size
    box_col = col // box_size

    # Check if the number is in the box by checking the row and column of the box
    for i in range(box_row * box_size, box_row * box_size + box_size):
        for j in range(box_col * box_size, box_col * box_size + box_size):
            if sudoku[i][j] == num:
                return False

    return True


def solve_sudoku(sudoku):
    # Find the next empty cell
    for row in range(sudoku_size):
        for col in range(sudoku_size):
            if sudoku[row][col] == 0:
                # Try all numbers from 1 to 9
                for num in range(1, sudoku_size + 1):
                    # Check if the number is valid
                    if is_valid(sudoku, row, col, num):
                        # If the number is valid, assign it to the cell
                        sudoku[row][col] = num
                        # Recursively call the function
                        if solve_sudoku(sudoku):
                            return True
                        # If the number is not valid, reset the cell to 0
                        sudoku[row][col] = 0
                # If no number is valid, return False
                return False
    # If the grid is full, return True
    return True


def print_sudoku(sudoku):
    # Print the grid
    for i in range(sudoku_size):
        for j in range(sudoku_size):
            print(sudoku[i][j], end=" ")
        print()


def save_sudoku(sudoku):
    # Save the grid to a file
    with open("sudoku9TBSolution.txt", "w") as file:
        for i in range(sudoku_size):
            for j in range(sudoku_size):
                file.write(str(sudoku[i][j]) + " ")
            file.write("\n")
    file.close()


# Solve the sudoku
print("Initial Sudoku:")
print_sudoku(sudoku)
print()

if solve_sudoku(sudoku):
    print("Solved Sudoku:")
    print_sudoku(sudoku)
    save_sudoku(sudoku)
else:
    print("No solution")
    file = open("sudoku9TBSolution.txt", "w")
    file.write("-1")
    file.close()
