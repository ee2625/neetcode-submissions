class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target == matrix[i][0]:
                return True
            elif matrix[i][0] < target <= matrix[i][-1]:
                for x in range(len(matrix[i])):
                    if target == matrix[i][x]:
                        return True
        return False
