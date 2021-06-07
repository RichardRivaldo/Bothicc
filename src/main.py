import numpy as np


class tic_tac_toe:
    bot_turn = False

    def __init__(self):
        self.board = np.full((3, 3), "_")

    def print_board(self):
        idx = len(self.board) - 1
        for row in self.board[::-1]:
            print("{idx}|".format(idx=idx), end="")
            for tile in row[:-1]:
                print(tile, end="|")
            print(row[-1], end="|\n")
            idx -= 1
        for i in range(len(self.board)):
            print("", i, end=" ")
        print("")

    def make_move(self, i, j):
        if self.board[i][j] != "_" or i > len(self.board) or j > len(self.board):
            print("Invalid Move!")
        else:
            if self.bot_turn:
                (self.board)[i][j] = "X"
                self.bot_turn = False
            else:
                (self.board)[i][j] = "O"
                self.bot_turn = True

    def row_won(self):
        for row in self.board:
            row = set(row)
            if len(row) == 1:
                if "X" in row:
                    return 1
                elif "O" in row:
                    return -1
        return 0

    def col_won(self):
        for i in range(len(self.board)):
            check = []
            for j in range(len(self.board)):
                check.append(self.board[j][i])
            col = set(check)
            if len(col) == 1:
                if "X" in col:
                    return 1
                elif "O" in col:
                    return -1
        return 0

    def diagonal_won(self):
        right_diag = set(np.diag(self.board))
        left_diag = set(np.diag(np.fliplr(self.board)))

        if len(right_diag) == 1:
            if "X" in right_diag:
                return 1
            elif "O" in right_diag:
                return -1
        if len(left_diag) == 1:
            if "X" in left_diag:
                return 1
            elif "O" in left_diag:
                return -1
        return 0

    def is_finished(self):
        row_eval = self.row_won()
        col_eval = self.col_won()
        diag_eval = self.diagonal_won()

        if row_eval == 1 or col_eval == 1 or diag_eval == 1:
            return (True, 1)
        elif row_eval == -1 or col_eval == -1 or diag_eval == -1:
            return (True, -1)
        elif not any("_" in row for row in self.board):
            return (True, 0)
        else:
            return (False, 0)

    def play(self):
        print("Welcome to the deepest hell of TicTacToe")
        print("The thicc demon, Bothicc, will be your opponent!")
        print("FIGHT AND BE VICTORIOUS, SOLDIER!\n")
        finished, player = self.is_finished()

        while not finished:
            tic_tac_toe.print_board()

            i = int(input("Enter i: "))
            j = int(input("Enter j: "))
            self.make_move(i, j)
            finished, player = self.is_finished()

        tic_tac_toe.print_board()
        if player == 1:
            print("Bothicc is superior!")
        elif player == -1:
            print("You're just lucky!")
        else:
            print("Bothicc is still superior!")


if __name__ == "__main__":
    tic_tac_toe = tic_tac_toe()
    tic_tac_toe.play()
