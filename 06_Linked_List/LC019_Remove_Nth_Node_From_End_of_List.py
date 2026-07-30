# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        dummy = ListNode(0, head)
        stop = length - n
        node = dummy
        move = 0
        while node:
            if move == stop:
                node.next = node.next.next
                break
            move += 1
            node = node.next
        return dummy.next
# 先遍历链表统计总节点长度，算出倒数第 n 个节点对应的正向位置。
# 借助虚拟头节点遍历至目标节点前驱，修改指针完成删除。
# Traverse the linked list once to calculate its total length, then locate the position of the nth node from the end.
# Use a dummy head node to reach the predecessor of the target node and adjust pointers to remove the node.

# Complexity Analysis
# Time Complexity: O(L), where L is the total number of nodes in the linked list. We traverse the list twice: one pass to count length, another to find the node to delete. Each node is visited at most twice.
# Space Complexity: O(1). We only create a constant number of temporary pointers and a dummy node, no extra data structures scaling with input size are used.

    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     curr, length = head, 0
    #     while curr:
    #         length += 1
    #         curr = curr.next
    #     dummy = ListNode(0, head)
    #     prev = dummy
    #     # 循环stop次，直接走到待删节点的前驱
    #     for _ in range(length - n):
    #         prev = prev.next
    #     prev.next = prev.next.next
    #     return dummy.next
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

# 设立虚拟头节点统一处理删除首节点边界，快慢指针初始均指向虚拟头。
# 快指针先走 n 步拉开间距，再同步移动至链表末尾，慢指针停在待删节点前驱，修改指针完成删除。
# Create a dummy head to simplify edge cases of removing the original first node; both fast and slow pointers start at this dummy node.
# Move the fast pointer n steps ahead first, then shift two pointers together until fast reaches the tail, adjust the next pointer of slow to skip the target node.

# Complexity Analysis
# Time Complexity: O(L), L refers to the total count of nodes in the linked list. The linked list is traversed only once. The fast pointer travels through all nodes, and the slow pointer moves part of the list, so the total operation is linear with input size.
# Space Complexity: O(1). Only a fixed number of pointer variables and one dummy node are created, no extra data structures that grow with the input length are used.
