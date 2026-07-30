# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total%10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# 同步遍历两条逆序链表，逐位取出数字相加，记录进位，用虚拟头节点构建结果链表。
# 链表遍历结束后若仍存在进位，单独新建节点存放最高进位，返回结果链表头部。
# Traverse two reversed lists simultaneously, sum digits with carry, build result list via dummy head node.
# Create an extra node to hold final carry if carry is non-zero after traversal, return the head of sum list.

# Complexity
# Time Complexity: O(max(m,n)), m and n are the lengths of l1 and l2, we traverse the longer list once.
# Space Complexity: O(max(m,n)), extra space for the output linked list, no other auxiliary space used.
