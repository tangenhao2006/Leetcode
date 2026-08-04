class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        if not self.stack:
            self.stack.append((value, value))
        else:
            current_min = min(value, self.stack[-1][1])
            self.stack.append((value, current_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


# 单个栈存储二元组，分别记录元素值和当前栈最小值。
# 每次入栈更新最小值，查询和弹出操作直接取用对应数据。

# Use a single stack to store tuples of value and current minimum.
# Update the minimum when pushing elements, and get data directly for other operations.

# Complexity
# Time Complexity: O(1) for all operations.
# Space Complexity: O(n).

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
# 用主栈保存全部元素，辅助栈同步记录过程中的最小值。
# 入栈、出栈时同步维护辅助栈，保证随时能快速获取最小值。

# Use one stack to store all elements and another to record minimum values.
# Maintain the two stacks synchronously to get the minimum in constant time.

# Complexity
# Time Complexity: O(1) for all operations.
# Space Complexity: O(n).

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
