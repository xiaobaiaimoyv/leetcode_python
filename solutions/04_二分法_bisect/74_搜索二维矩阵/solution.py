#本质来说，就是化二维为一维，比如a[m][n]可以近似看作a[k] k // len(a[0]) = m ; k % len(a[0]) = n
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = (l + r) // 2
            a = mid // n
            b = mid - a * n
            if(matrix[a][b] >= target):
                r = mid - 1
            else:
                l = mid + 1
        ax = l // n
        bx = l % n
        if ax == m or bx == n:
            return False
        return matrix[ax][bx] == target


        