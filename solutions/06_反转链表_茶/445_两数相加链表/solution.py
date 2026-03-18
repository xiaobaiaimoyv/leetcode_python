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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 反转输入链表
        l1_rev = self.reverseList(l1)
        l2_rev = self.reverseList(l2)

        sec = 0
        dummy = ListNode(0)  # 虚拟头节点
        curr = dummy

        a, b = l1_rev, l2_rev

        # 2. 只要有值或者有进位，就继续计算
        while a or b or sec:
            val1 = a.val if a else 0
            val2 = b.val if b else 0

            # 计算总和与进位
            total = val1 + val2 + sec
            sec = total // 10

            # 创建新节点并连接
            curr.next = ListNode(total % 10)
            curr = curr.next

            # 指针后移
            if a: a = a.next
            if b: b = b.next

        # 3. 最后还要把结果反转回来（因为题目要求高位在前）
        return self.reverseList(dummy.next)