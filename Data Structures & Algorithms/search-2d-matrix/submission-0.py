class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        mid = 0
        while (end >= start):
            mid = (end + start) //2
            if (matrix[mid][0] < target and matrix[mid][len(matrix[0]) - 1] > target):
                break
            elif (matrix[mid][len(matrix[0]) - 1] < target):
                start = mid + 1
            elif (matrix[mid][0] > target ):
                end = mid - 1
            else: 
                return True
        start = 1
        end = len(matrix[mid]) - 2
        while (end >= start):
            mid2 = (start + end) // 2
            if (matrix[mid][mid2] > target):
                start = mid2 + 1
            elif (matrix[mid][mid2] < target):
                end = mid2 - 1
            else:
                return True
        return False