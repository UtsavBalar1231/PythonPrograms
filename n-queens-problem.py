#!/usr/bin/env python

# The N-queens puzzle is the problem of placing N queens on an N × N chessboard such that no two queens
# attack each other.
# Given an integer N (1 ≤ N ≤ 10), return all distinct solutions to the N-queens puzzle. The table below
# shows the number of solutions and the number of unique solutions (without any rotations and reflections).
#
# Each solution contains a distinct board configuration of the N-queens’ placement, where ‘1’ and ‘0’ both
# indicate a queen and an empty space, resultpectively. Your program must include a class called Puzzle which
# includes the following methods:
# findASafePlace: method to find a safe place
# isSafe: method to check if a position is safe
# placeQueen: method to place a queen on the board
# removeQueen: method to remove a queen from the board
# displayBoard: method to display queens on the board


class Puzzle:
    def __init__(self, n):
        # n is the number of queens
        self.n = n
        # initialize board with 0s
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.boards = []

    def findASafePlace(self, row, col):
        # check if a queen can be placed on board[row][col]
        if self.isSafe(row, col):
            self.placeQueen(row, col)
            return True
        return False

    def isSafe(self, row, col):
        # check this row on left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        # check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        # check lower diagonal on left side
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def placeQueen(self, row, col):
        # place a queen on board[row][col]
        self.board[row][col] = 1

    def removeQueen(self, row, col):
        # remove a queen from board[row][col]
        self.board[row][col] = 0
        
    def displayBoard(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()
        print()

    def solveNQ(self, col):
        # base case: If all queens are placed
        if col >= self.n:
            self.boards.append(self.board)
            self.displayBoard()
            return True
        result = False
        # Consider this column and try placing this queen in all rows one by one
        for i in range(self.n):
            if self.findASafePlace(i, col):
                result = self.solveNQ(col + 1) or result
                self.removeQueen(i, col)
        return result

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    puzzle = Puzzle(n)
    puzzle.solveNQ(0)
    print("Number of solutions: ", len(puzzle.boards))