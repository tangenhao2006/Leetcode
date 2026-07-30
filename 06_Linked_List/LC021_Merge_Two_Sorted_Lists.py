# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return dummy.next

# 虚拟头+尾指针双指针遍历两条有序链表，每次把更小节点接到尾部，同步后移对应链表指针与尾指针；
# 一条链表遍历完毕后直接拼接剩余节点，dummy固定保存链表起点，循环结束返回dummy.next作为合并链表头节点。
# Traverse two sorted linked list with dummy head and temp pointer. Attach smaller node to tail each iteration,
# shift corresponding list pointer and temp pointer forward. Link remaining nodes after one list exhausted.
# Dummy permanently stores entry of merged list, return dummy.next as new head after loop ends.

# Complexity
# Time Complexity: O(m + n)
# Space Complexity: O(1)
