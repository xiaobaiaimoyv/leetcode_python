#如果不用bisect_left，应该怎么实现呢？

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = bisect_left(nums, target)
        b = bisect_left(nums, target + 1)
        if a == len(nums) or nums[a] != target or  nums[0] > target:
            return [-1, -1]
        else:
            return[a, b - 1] 

        