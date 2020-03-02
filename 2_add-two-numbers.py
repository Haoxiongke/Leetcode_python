# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # maybe standard version
    def _addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 这里一开始不做l1、l2非空判断，题意表明非空链表
        # 记录是否需要增加新节点，或在链表下一个节点是否需要加1，同时记录链表同级节点的和
        carry = 0
        # 这里的执行顺序是res = ListNode(0), pre = res
        res = pre = ListNode(0)
        # 判断l1、l2、carry是否有值，carry有值的话需要增加新节点，或在链表下一个节点需要加1
        while l1 or l2 or carry:
            # 判断l1是否有值
            if l1:
                carry += l1.val
                l1 = l1.next
            # 判断l2是否有值
            if l2:
                carry += l2.val
                l2 = l2.next
            # carry有同级节点的和
            # divmod返回商与余数的元组，拆包为carry和val
            # carry有值的话需要增加新节点，或在链表下一个节点需要加1,在循环中会用到
            carry, val = divmod(carry, 10)
            # 新建链表节点
            # 这里是n.next = ListNode(val), n = n.next()
            pre.next = pre = ListNode(val)
        # res等价于pre，res.val=0，所以返回res.next
        return res.next


if __name__ == '__main__':
    # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(5)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)
    # 获取返回值的链表
    res = sol._addTwoNumbers(l1, l2)
    # 循环遍历出来
    while res:
        print(res.val)
        res = res.next

    # p = dummy = ListNode(-1)
    # carry = 0
    # while l1 and l2:
    #     p.next = ListNode(l1.val + l2.val + carry)
    #     carry = p.next.val / 10
    #     p.next.val %= 10
    #     p = p.next
    #     l1 = l1.next
    #     l2 = l2.next
    #
    # res = l1 or l2
    # while res:
    #     p.next = ListNode(res.val + carry)
    #     carry = p.next.val / 10
    #     p.next.val %= 10
    #     p = p.next
    #     res = res.next
    # if carry:
    #     p.next = ListNode(1)
    # return dummy.next

    # # shorter version
    # def addTwoNumbers(self, l1, l2):
    #   p = dummy = ListNode(-1)
    #   carry = 0
    #   while l1 or l2 or carry:
    #     val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
    #     carry = val / 10
    #     p.next = ListNode(val % 10)
    #     l1 = l1 and l1.next
    #     l2 = l2 and l2.next
    #     p = p.next
    #   return dummy.next
