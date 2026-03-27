class Solution:
    def isValid(self, s: str) -> bool:
        # 奇数长度直接排除，小小的性能优化
        if len(s) % 2 != 0:
            return False

        # 使用字典建立匹配关系，Key 为右括号，Value 为左括号
        # 这样判断 "x in dic" 就能秒懂它是不是一个“待匹配的右括号”
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []

        for x in s:
            if x in dic:
                # 如果是右括号，检查栈顶
                # 如果栈为空，或者栈顶不是对应的左括号，直接失败
                if not stack or stack[-1] != dic[x]:
                    return False
                stack.pop()
            else:
                # 如果是左括号，直接入栈
                stack.append(x)

        # 最终栈为空则合法
        return not stack