class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = collections.defaultdict(set)
        colset = collections.defaultdict(set)
        squareset = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if int(board[i][j]) < 1 or int(board[i][j]) > 9 or (board[i][j] in rowset[i]) or (board[i][j] in colset[j]) or (board[i][j] in squareset[(i // 3,j // 3)]):
                    return False
                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                squareset[(i//3, j//3)].add(board[i][j])
        
        return True

