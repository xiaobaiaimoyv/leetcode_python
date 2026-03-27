class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # left: 已使用的左括号数, right: 已使用的右括号数
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                res.append(S)
                return

            # 只要左括号还没用完，就可以加左括号
            if left < n:
                backtrack(S + '(', left + 1, right)

            # 只有当右括号数量小于左括号时，加右括号才是合法的
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack("", 0, 0)
        return res