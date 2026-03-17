class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = nums[0]
        nums.sort()
        k = nums.index(a)
        b = bisect_left(nums, target)
        if b == len(nums) or nums[b] != target or nums[0] > target:
            return -1
        else:
            return (b - k) % len(nums)
        