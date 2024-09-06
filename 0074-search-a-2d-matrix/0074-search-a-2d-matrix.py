class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowSize = len(matrix)
        colSize = len(matrix[0])

        top = 0
        bottom = rowSize - 1

        while bottom >= top:
            row = (bottom + top) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        
        if not bottom >= top:
            return False

        row = (bottom + top) // 2
        l = 0
        r = colSize - 1
        while r >= l:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False


        


        