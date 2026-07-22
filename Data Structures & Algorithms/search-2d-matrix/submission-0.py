class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                l = 0
                r = n-1
                while l<=r:
                    mid = (l+r)//2
                    if target == matrix[i][mid]:
                        return True
                    elif target < matrix[i][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False 