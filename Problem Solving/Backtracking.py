"""
Backtracking and recursion are related concepts, but they are not the same thing.

Recursion is a programming technique where a function calls itself in order to solve a problem.
Recursion can be used to solve a wide variety of problems, such as calculating factorials, traversing binary trees,
and searching through lists.

Backtracking is a specific problem-solving technique that involves exploring all possible solutions to a problem by
incrementally building candidates and abandoning them as soon as it determines that they cannot
possibly lead to a valid solution. Backtracking is often implemented using recursion,
but it is not limited to recursive algorithms.
"""


# --------------------------------------------------------------------------------------------------
# Suppose you have a list of numbers, and you want to find all possible subsets of the list.

# Recursive Solution
def subsets(nums):
    if not nums:
        return [[]]
    else:
        result = []
        for subset in subsets(nums[1:]):
            result.append(subset)
            result.append([nums[0]] + subset)
        return result


print("Recursion: Subsets")
print(subsets([1, 3, 9]))


# Backtracking Solution
def subsets(nums):
    def backtrack(first=0, current=[]):
        result.append(current[:])
        for i in range(first, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    result = []
    backtrack()
    return result


print("Backtracking: Subsets")
print(subsets([1, 3, 8]))


# --------------------------------------------------------------------------------------------------------------
# Backtracking algorithm for finding all possible permutations of a list of elements:

def permute(nums):
    def backtrack(count):
        if count == n:
            output.append(nums[:])
        for i in range(count, n):
            nums[count], nums[i] = nums[i], nums[count]
            backtrack(count + 1)
            nums[count], nums[i] = nums[i], nums[count]

    n = len(nums)
    output = []
    backtrack(0)
    return output


print("Backtracking: Permute")
print(permute([0, 4, 8]))


# ----------------------------------------------------------------------------------------------------------------
# Backtracking solution for generating all possible combinations of a set of characters:


def combinations(chars):
    def backtrack(start=0, current=""):
        result.append(current)
        for i in range(start, len(chars)):
            backtrack(i + 1, current + chars[i])

    result = []
    backtrack()
    return result


print("Backtracking: Combination")
print(combinations("xyz"))


# ----------------------------------------------------------------------------------------------------------------
# Backtracking solution for generating all possible permutations of a set of characters:
def permutations(chars):
    def backtrack(current=[]):
        if len(current) == len(chars):
            result.append(current[:])
        else:
            for char in chars:
                if char not in current:
                    current.append(char)
                    backtrack(current)
                    current.pop()

    result = []
    backtrack()
    return result


print("Backtracking: Permutations")
print(permutations("xyz"))


# ----------------------------------------------------------------------------------------------------------------
# find all possible ways to split a string into words, given a dictionary of valid words:

def word_break(s, word_dict):
    def backtrack(start=0, current=[]):
        if start == len(s):
            result.append(" ".join(current))
        else:
            for i in range(start, len(s)):
                word = s[start:i + 1]
                if word in word_dict:
                    current.append(word)
                    backtrack(i + 1, current)
                    current.pop()

    result = []
    backtrack()
    return result


print("Backtracking: Word_break")
print(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))


# -----------------------------------------------------------------------------------------------------------------

# Solve n quene poblem on n * n board

def solve_n_queens(n):
    board = [['.' for j in range(n)] for i in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    def is_valid(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        return True

    backtrack(0)
    return solutions


import pprint

print("N Queens Problem")
pprint.pprint(solve_n_queens(5))


# ----------------------------------------------------------------------------------------------------------------
# n queens another approach
def solve_n_queens(n):
    def place_queen(board, row, solutions):
        if row == len(board):
            solutions.append([row[:] for row in board])
            return

        for col in range(len(board)):
            if is_valid_move(board, row, col):
                board[row][col] = 1
                place_queen(board, row + 1, solutions)
                board[row][col] = 0

    def is_valid_move(board, row, col):
        for i in range(row):
            if board[i][col]:
                return False
            for j in range(len(board)):
                if abs(row - i) == abs(col - j) and board[i][j]:
                    return False
        return True

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    place_queen(board, 0, solutions)
    return solutions


print("N Queens Problem")
pprint.pprint(solve_n_queens(4))

# ---------------------------------------------------------------------------------------------------------------

"""
SUDOKU
"""


def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking.

    Args:
        board (list): A 9x9 nested list representing the Sudoku board. 0 represents an empty cell.

    Returns:
        bool: True if a solution is found, False otherwise.
    """

    def find_empty_cell(board):
        """
        Finds the next empty cell on the board.

        Args:
            board (list): A 9x9 nested list representing the Sudoku board. 0 represents an empty cell.

        Returns:
            tuple: A tuple containing the row and column of the next empty cell, or (None, None) if there are no more empty cells.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return (None, None)

    def is_valid_move(board, row, col, num):
        """
        Checks if a number can be placed in a given cell.

        Args:
            board (list): A 9x9 nested list representing the Sudoku board. 0 represents an empty cell.
            row (int): The row of the cell to check.
            col (int): The column of the cell to check.
            num (int): The number to check.

        Returns:
            bool: True if the number can be placed in the cell, False otherwise.
        """
        # Check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False

        return True

    # Find the next empty cell on the board
    row, col = find_empty_cell(board)

    # If there are no more empty cells, the puzzle is solved
    if row is None:
        return True

    # Try all possible values for the empty cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            # Place the number on the board
            board[row][col] = num

            # Recursively try to fill in the rest of the board
            if solve_sudoku(board):
                return True

            # If no solution is found, backtrack and try a different number
            board[row][col] = 0

    # If all numbers have been tried and no solution is found, the puzzle is unsolvable
    return False


board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
         ]

solve_sudoku(board)

print("Sudoku: Backtracking")
for row in board:
    print(row)


# --------------------------------------------------------------------------------------------------------------
# This code finds all possible subsets of a given set of integers that add up to a given target sum, using backtracking

def subset_sum(nums, target):
    def find_subsets(nums, target, subset, solutions):
        if sum(subset) == target:
            solutions.append(subset[:])
            return

        if sum(subset) > target:
            return

        for i in range(len(nums)):
            subset.append(nums[i])
            find_subsets(nums[i + 1:], target, subset, solutions)
            subset.pop()

    solutions = []
    find_subsets(nums, target, [], solutions)
    return solutions


print("Subset_sum: Backtracking")
pprint.pprint(subset_sum([1, 2, 3, 4, 5], 7))

# -----------------------------------------------------------------------------------------
"""
ARRANGING ITEMS WITH A CONSTRAINTS

You want to find all the possible ways of arranging 2 boys and 1 girl on 3 benches. 
Constraint: Girl should not be on the middle bench. solve in python using backtracking
"""


def arrange_backtrack(solution, input):
    # Define a helper function to check if a partial solution is valid
    def is_valid(solution):
        # Check if g is in the middle
        if len(solution) == 2 and solution[1] == "g":
            return False
        # Check if there are any duplicates
        if len(solution) != len(set(solution)):
            return False
        # Otherwise, the solution is valid
        return True

    # Define a recursive function to generate all possible arrangements
    # Call the backtrack function with an empty solution and the input list
    # If the solution is complete, print it

    if len(solution) == len(input):
        print(solution)
        return
    # Otherwise, try each element in the input list
    for element in input:
        # Add the element to the solution
        solution.append(element)
        # If the solution is valid, recurse on the remaining input
        if is_valid(solution):
            arrange_backtrack(solution, input)
        # Remove the element from the solution
        solution.pop()


print("Arrange Boys and Girl: Backtracking")
pprint.pprint(arrange_backtrack([], ["b1", "b2", "g"]))

# --------------------------------------------------------------------------------------------------------------
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.

def generateParenthesis(n):
    def helper(n, open_brackets, close_brackets, combination, res):
        if len(combination) == n * 2:
            res.append(combination)
            return
        if open_brackets < n:
            helper(n, open_brackets + 1, close_brackets, combination + "(", res)
        if close_brackets < open_brackets:
            helper(n, open_brackets, close_brackets + 1, combination + ")", res)

    res = []
    helper(n, 0, 0, "", res)
    return res


print("Generate_parenthesis: backtracking")
print(generateParenthesis(2))

# -------------another approach----------------------------

def valid_parenthesis_generator(n):
    def backtracker(res, opened, closed, strings, n):
        if opened == n and closed == opened:
            res.append(strings)
        if opened < n:
            backtracker(res, opened + 1, closed, strings + "(", n)
        if closed < opened:
            backtracker(res, opened, closed + 1, strings + ")", n)

    results = []
    opened = 0
    closed = 0
    strings = ""
    backtracker(results, opened, closed, strings, n)

    return results


answer = valid_parenthesis_generator(5)
print(f"{len(answer)} total possibilities")
print(answer)