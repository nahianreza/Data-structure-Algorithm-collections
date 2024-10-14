class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rowSize = len(board)
        colSize = len(board[0])

        visited = set()

        directions = [(-1,0), (1, 0), (0,1), (0, -1)]
        index = 0

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r >= rowSize or r < 0 or c >= colSize or c < 0 or (r, c) in visited or board[r][c] != word[index]:
                return False


            visited.add((r,c))

            for x, y in directions:
                if dfs(r + x, c + y, index + 1):
                    return True

            visited.remove((r,c))

        
        for i in range(rowSize):
            for j in range(colSize):
                if board[i][j] == word[index]:
                    if dfs(i, j, index):
                        return True

        return False



        