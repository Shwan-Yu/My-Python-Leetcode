class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row, self.col, self.diagOne, self.diagTwo, self.n = [0]*n, [0]*n, 0, 0, n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        mark = 1 if player == 1 else -1
        self.row[row] += mark; self.col[col] += mark
        if row == col: self.diagOne += mark
        if row+col == self.n-1: self.diagTwo += mark # do not use elif, because they are two different diagonals.
        if self.n in [self.row[row], self.col[col], self.diagOne, self.diagTwo]: return 1
        elif -self.n in [self.row[row], self.col[col], self.diagOne, self.diagTwo]: return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
