class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(mat) - 1
        
        while top <= bottom:
            mid = (top + bottom) // 2
            
            # 找到当前 mid 行的最大值（全行最大）
            max_col = 0
            for j in range(len(mat[mid])):
                if mat[mid][j] > mat[mid][max_col]:
                    max_col = j
            
            # 检查上下邻居（注意越界处理）
            is_greater_than_top = (mid == 0) or (mat[mid][max_col] > mat[mid-1][max_col])
            is_greater_than_bottom = (mid == len(mat)-1) or (mat[mid][max_col] > mat[mid+1][max_col])
            
            if is_greater_than_top and is_greater_than_bottom:
                # 找到了！它比左右大（因为是行最大），比上下大（验证过了）
                return [mid, max_col]
            elif not is_greater_than_top:
                # 上面更高，说明峰值在上半区
                bottom = mid - 1
            else:
                # 下面更高，说明峰值在下半区
                top = mid + 1
                
        return [-1, -1]