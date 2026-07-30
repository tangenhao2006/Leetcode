"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        curr = head
        mapping = {}
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new_node = mapping[curr]
            new_node.next = mapping.get(curr.next)
            new_node.random = mapping.get(curr.random)
            curr = curr.next
        return mapping[head]
# 哈希映射实现链表深拷贝，分两次遍历原链表完成复制
# 第一次遍历创建全部全新拷贝节点，用哈希表建立原节点与对应新节点的映射关系
# 第二次遍历借助映射表，为每个拷贝节点绑定next指针与random随机指针，保证新链表只引用新节点

# Traverse the original linked list twice to implement deep copy with hash map.
# First pass creates all brand-new copied nodes and builds a map between original nodes and copies.
# Second pass assigns next and random pointers for each copied node via the mapping table, ensuring all pointers only reference new nodes.

# Complexity (Hash Map Solution)
# Time Complexity: O(n), we traverse the linked list exactly two times, each operation inside loops is O(1)
# Space Complexity: O(n), extra hash map stores mapping of all n original nodes to copied nodes
