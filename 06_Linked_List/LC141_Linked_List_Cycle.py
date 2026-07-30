# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

# 遍历链表，用集合记录所有访问过的节点；每次先判断当前节点是否已经存在集合中，存在则代表重复访问，链表存在环；
# 不存在则将当前节点存入集合，继续向后遍历；若遍历到空节点说明链表无环，返回False。
# Traverse linked list, store all visited nodes in a set. Check if current node exists in set first;
# If exists, the node is revisited meaning cycle exists. If not, add node to set and move forward.
# If traversal reaches null node, no cycle exists, return False.

# Complexity
# Time Complexity: O(n)
# Space Complexity: O(n)

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 快慢双指针从头同步出发，慢指针每次走一步，快指针每次走两步；无环时快指针会先遍历到空节点终止循环；
# 存在环时快指针会在环内持续追赶慢指针，两指针必然相遇，相遇即证明链表存在环。
# Start slow and fast pointers at head. Slow moves 1 step, fast moves 2 steps per iteration.
# If no cycle, fast pointer reaches null to exit loop. If cycle exists, fast will catch slow inside cycle, collision means cycle exists.

# Complexity
# Time Complexity: O(n)
# Space Complexity: O(1)
