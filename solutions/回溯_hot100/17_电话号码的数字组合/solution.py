class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        refer = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        res = []
        def trace(method, index):
            if len(method) == len(digits):
                res.append(method[:])
                return
            for x in refer[int(digits[index])]:
                method = method + x
                trace(method, index + 1)
                method = method[:-1]
        trace("", 0)
        return res

        