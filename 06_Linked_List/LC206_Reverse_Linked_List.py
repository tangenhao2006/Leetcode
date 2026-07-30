# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

# 双指针遍历链表，每次先保存下一个节点，将当前节点指向前一个节点，同步移动前后指针，循环结束后 prev 是反转链表的头节点。
# Traverse the linked list with two pointers. Store the next node before reversing current pointer, shift both pointers forward, return prev as new head after loop ends.

# Complexity
# Time Complexity: O(n)
# Space Complexity: O(1)
