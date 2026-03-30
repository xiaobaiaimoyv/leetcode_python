class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n  # 特判一下小数值

        plt = [0] * (n + 1)
        plt[1], plt[2] = 1, 2
        for i in range(3, n + 1):
            plt[i] = plt[i - 1] + plt[i - 2]
        return plt[n]