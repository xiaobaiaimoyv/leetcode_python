class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def trace(method, index):
            if len(method) <= len(nums):
                res.append(method[:])
                
            for i in range(index, len(nums)):
                method.append(nums[i])
                trace(method, i+1)
                method.pop()
        trace([], 0)
        return res
        