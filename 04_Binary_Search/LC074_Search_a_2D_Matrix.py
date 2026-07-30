class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # row.  3
        n = len(matrix[0]) # column. 4
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n  # each row has n numbers, mid // n shows which row
            column = mid % n
            value = matrix[row][column]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# 将有序二维矩阵视作一维有序数组，使用二分查找。通过整除、取模把一维下标转为行列坐标，逐步缩小查找范围。
# Treat the 2D sorted matrix as a 1D array and use binary search. Convert 1D index to row and column to find the target.

# Complexity
# Time Complexity: O(log(m * n))
# Space Complexity: O(1)
