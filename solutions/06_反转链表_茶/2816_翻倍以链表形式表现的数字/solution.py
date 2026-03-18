class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.reverseList(head)
        sec = 0
        dummy = ListNode(0)
        p0 = dummy
        res = l

        # 注意这里：即便 res 走完了，只要还有进位 (sec > 0)，循环就会继续
        while res or sec:

            # 【注意点 1】：防御性取值
            # 作用：如果链表已经处理完（res 为 None），但还有进位需要计算，
            # 我们就把当前位当做 0。如果不加这个 if，访问 None.val 会直接报错。
            val = res.val if res else 0

            total = val * 2 + sec
            sec = total // 10
            p0.next = ListNode(total % 10)
            p0 = p0.next

            # 【注意点 2】：防御性移动指针
            # 作用：只有当 res 还没走到尽头时，才让它向后移位。
            # 如果不加这个 if，在处理最后一次进位时，对 None 执行 .next 会报错。
            if res:
                res = res.next

        return self.reverseList(dummy.next)