# Implement Binary Search to find the row to look for
# Impement Binary Search to find the value
# If value not found, return False
# Time Complexity O(log(mxn))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = len(matrix), len(matrix[0])
        
        top = 0
        bottom = row - 1
        
        targetRow = 0
        while bottom >= top:
            targetRow = (top + bottom) // 2
            if matrix[targetRow][0] <= target <= matrix[targetRow][column -1]:
                break
            elif target < matrix[targetRow][0]:
                bottom = targetRow - 1
            elif target > matrix[targetRow][column - 1]:
                top = targetRow + 1
        
        l, r = 0, column - 1
        
        
        while r >= l:
            mid = (l + r) // 2
            midVal = matrix[targetRow][mid]
            if midVal == target:
                return True
            elif midVal > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return False
                
        

        


        