class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board: return 0
        m, n, res = len(board), len(board[0]), 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    # if previous X has already been counted as a battleship, then we count it this time as 0.
                    tmp = 0 if (i>0 and board[i-1][j] == "X") or (j>0 and board[i][j-1] == "X") else 1
                    res += tmp
        return res
