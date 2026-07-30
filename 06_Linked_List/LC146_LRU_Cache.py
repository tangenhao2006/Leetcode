class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.latest.prev
        next_node = self.latest
        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            delete_node = self.oldest.next
            self.remove(delete_node)
            del self.cache[delete_node.key]

# 用哈希字典存储 key 与链表节点映射，实现 O (1) 查找；双向链表记录数据访问先后，虚拟头尾节点简化边界操作。查询时摘除节点重插至链表尾部标记为最新；更新 / 新增数据同样放到尾部；缓存容量溢出时删除虚拟头后第一个最久未使用节点，并同步清理字典映射。
# We use a hash map to map keys to doubly linked list nodes for instant lookup. A doubly linked list with dummy head and tail maintains the recency of data. For get operation, detach the target node and reinsert it before dummy tail to mark it as recently used. For put, update existing node value or create new node then insert to the tail. If cache exceeds capacity, remove the least recently used node right after dummy head and delete its key from hash map.

# Complexity
# Time Complexity: Average O(1) for both get and put operations
# Space Complexity: O(capacity), extra space for hash map and doubly linked list nodes


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
