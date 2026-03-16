class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def f(k:int) -> int:
            cnt = 1
            a = price[0]
            for x in price:
                if x - a >= k:
                    cnt += 1
                    a = x
            return cnt
        price.sort()
        left = 0
        right = max(price) - min(price)
        while left <= right:
            mid = (left + right) // 2
            if f(mid) >= k:
                left = mid + 1
            else:
                right = mid - 1
        return right