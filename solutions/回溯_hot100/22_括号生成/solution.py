class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        total = 0

        def trace(method):
            nonlocal total
            if len(method) == 2 * n:
                if total == 0:
                    res.append(method[:])
                return
            choice = "()"
            for x in choice:
                method = method + x
                temp = total
                if x == "(":
                    total += 1
                else:
                    total -= 1
                if total < 0:
                    continue
                trace(method)
                method = method[:-1]
                total = temp

        trace("")
        return res




