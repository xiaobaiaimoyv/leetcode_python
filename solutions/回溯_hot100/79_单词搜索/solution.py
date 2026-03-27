class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)  # 行数
        m = len(board[0])  # 列数
        used = [[False] * m for _ in range(n)]

        def trace(x, r, c):
            # 找到所有字符了，成功！
            if x == len(word):
                return True

            # 越界检查、字符不匹配、或者已经用过，直接回退
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != word[x] or used[r][c]:
                return False

            # --- 前序动作：标记已使用 ---
            used[r][c] = True

            # 尝试四个方向：上下左右 (不用双重循环，避免斜向移动)
            res = trace(x + 1, r + 1, c) or \
                  trace(x + 1, r - 1, c) or \
                  trace(x + 1, r, c + 1) or \
                  trace(x + 1, r, c - 1)

            # --- 后序动作：回溯（状态重置） ---
            used[r][c] = False

            return res

        # 遍历起点
        for i in range(n):
            for j in range(m):
                if trace(0, i, j):
                    return True

        return False