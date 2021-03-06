# 面试题25：合并两个排序的链表
# 题目：输入两个递增排序的链表，合并这两个链表并使新链表中的节
# 点仍是递增排序的。例如 ，输入图3.11 中的链表1和链表2，则合并之
# 后的升序链表入链表3所示。
# struct ListNode
# {
#     int m_nVlaue;
#     ListNode* m_pNext;
# }

# 链表1:   1 -> 3 -> 5 -> 7
# 链表2:   2 -> 4 -> 6 -> 8
# 链表3：  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_list(l1, l2):
    # 一个为None，就返回另一个
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    l = None
    head = l
    while l1 is not None and l2 is not None:  # 两个链表都存在的情况
        if l1.value < l2.value:
            candidate_node = l1
            l1 = l1.next
        else:
            candidate_node = l2
            l2 = l2.next

        if l is None:  # 头结点，初始化链表
            l = candidate_node
            l.next = None
            head = l
        else:
            candidate_node.next = l.next
            l.next = candidate_node
            l = l.next
    if l1 is not None:
        l.next = l1

    if l2 is not None:
        l.next = l2
    return head


if __name__ == "__main__":
    l1_5 = Node(10)
    l1_4 = Node(7, l1_5)
    l1_3 = Node(5, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)

    l2_3 = Node(6)
    l2_2 = Node(6, l2_3)
    l2_1 = Node(5, l2_2)
    l1_1 = merge_list(l1_1, l2_1)

    while l1_1 is not None:
        print(l1_1.value)
        l1_1 = l1_1.next
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i*i for i in A])

# 递归版本

# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1
#         elif l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2
