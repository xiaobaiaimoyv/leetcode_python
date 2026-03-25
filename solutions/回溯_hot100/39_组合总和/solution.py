class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def trace(method , index):
            if(sum(method) == target):
                res.append(method[:])
                return
            if(sum(method) > target):
                return
            for i in range(index,len(candidates)):
                x = candidates[i]
                method.append(x)
                trace(method, i)
                method.pop()
        trace([], 0)
        return res