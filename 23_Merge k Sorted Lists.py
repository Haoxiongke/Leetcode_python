"""
Problem:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        合并K个排序链表
        :param lists: List[ListNode]
        :return: ListNode
        """
        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        if res == []:
            return []
        res.sort()
        l = ListNode(0)
        first = l
        while res:
            l.next = ListNode(res.pop(0))
            l = l.next
        return first.next



if __name__ == '__main__':
    print(Solution().mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]))
