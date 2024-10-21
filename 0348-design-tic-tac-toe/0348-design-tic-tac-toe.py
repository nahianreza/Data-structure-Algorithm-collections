class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.col = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0
        self.length = n


        

    def move(self, row: int, col: int, player: int) -> int:
        cur = 1 if player == 1 else - 1

        self.rows[row] += cur
        self.col[col] += cur

        if row == col:
            self.diagonal += cur
        
        if row == self.length - 1 - col:
            self.antiDiagonal += cur

        if abs(self.rows[row]) == self.length or abs(self.col[col]) == self.length or abs(self.diagonal) == self.length or abs(self.antiDiagonal) == self.length:
            return player
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)