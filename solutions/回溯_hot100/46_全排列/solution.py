class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def track(method):
            if len(method) == len(nums):
                res.append(method[:])
                return
            for i, x in enumerate(nums):
                if used[i]:
                    continue
                method.append(x)
                used[i] = True        
                track(method)
                method.pop()
                used[i] = False
        track([])
        return res