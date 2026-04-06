class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Apply binary search to the matrix as if it was one row
        rows = len(matrix)
        cols = len(matrix[0])
        
        size = rows * cols
        l, r = 0, size - 1

        while l <= r:
            mid = (l + r) // 2
            n = matrix[mid // cols][mid % cols]
            if target == n:
                return True
            elif target < n:
                r = mid - 1
            else:
                assert target > n
                l = mid + 1

        return False