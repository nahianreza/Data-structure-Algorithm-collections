class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]

        self.playerMap = {1: 'X', 2: '0'}

        self.n = n


        

    def move(self, row: int, col: int, player: int) -> int:
        winner = 0 
        moveChar = self.playerMap[player]
        self.board[row][col] = moveChar
        
        for i in range(self.n):
            if self.board[i][col] != moveChar:
                break
        else:
            return player
        
        for j in range(self.n):
            if self.board[row][j] != moveChar:
                break
        else:
            return player
        
        
        for d in range(self.n):
            if self.board[d][d] != moveChar:
                break
        else:
            return player
            

        for nd in range(self.n):
            if self.board[nd][self.n -1 - nd] != moveChar:
                break
        else:
            return player
        
        
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)