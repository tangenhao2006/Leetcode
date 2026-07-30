# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        prev = None
        curr = mid
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev

        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

# 三步原地重排链表：快慢指针找到链表中点并截断前后两段；双指针反转后半段链表；循环交替合并两段链表，提前缓存两段原始后继节点，优先使用缓存值更新指针，避免链表成环导致死循环，全程仅修改节点指针。
# Three-step in-place reorder: Find midpoint and split list with two pointers; reverse second half; interleave merge two segments, cache original next nodes in advance and update pointers by cached value to avoid cycle infinite loop.

# Complexity
# Time Complexity: O(n)
# Space Complexity: O(1)
