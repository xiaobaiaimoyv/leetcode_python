方法一：递归写法
反转链表 l 
1

 。
反转链表 l 
2

 。
调用 2. 两数相加 的代码，得到链表 l 
3

 。
反转链表 l 
3

 ，返回 l 
3

  作为答案。
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head  # 把下一个节点指向自己
        head.next = None  # 断开指向下一个节点的连接，保证最终链表的末尾节点的 next 是空节点
        return new_head

    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwo(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界：l1 和 l2 都是空节点
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        carry += l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = carry % 10  # 每个节点保存一个数位
        l1.next = self.addTwo(l1.next, l2.next if l2 else None, carry // 10)  # 进位
        return l1
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)  # l1 和 l2 反转后，就变成【2. 两数相加】了
        l3 = self.addTwo(l1, l2)
        return self.reverseList(l3)
复杂度分析
时间复杂度：O(n)，其中 n 为 l 
1

  长度和 l 
2

  长度的最大值。
空间复杂度：O(n)。递归需要 O(n) 的栈空间。

作者：灵茶山艾府
链接：https://leetcode.cn/problems/add-two-numbers-ii/solutions/2328330/fan-zhuan-lian-biao-liang-shu-xiang-jia-okw6q/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。