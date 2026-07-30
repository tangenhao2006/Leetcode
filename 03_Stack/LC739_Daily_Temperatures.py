class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Get the number of days (length of temperatures list)
        n = len(temperatures)
        # Initialize answer list with zeros, one element per day
        answer = [0] * n
        # Use a stack to store indices of days we haven't found a warmer day for
        stack = []

        # Iterate through each day with index i
        for i in range(n):
            # Get the temperature of the current day
            temp = temperatures[i]
            # While there are days in the stack and current temp is higher than the stack's top day's temp
            while stack and temp > temperatures[stack[-1]]:
                # Pop the index of the previous colder day
                prev_day = stack.pop()
                # Calculate days to wait: current index - previous day index
                answer[prev_day] = i - prev_day
            # Push current day index to stack, waiting for a warmer day in the future
            stack.append(i)

        # Return the list of waiting days
        return answer

# 初始化一个全为 0 的答案数组，并用栈存储还未找到更暖天气的日期索引。
# 遍历每一天，只要当前气温高于栈顶日期的气温，就弹出栈顶并计算等待天数，更新答案数组。
# 将当前日期压入栈，等待后续处理，遍历结束后返回答案数组。

# Initialize an answer list filled with zeros, and use a stack to store indices of days that have not yet found a warmer day.
# Iterate through each day; while the current temperature is higher than the temperature of the day at the top of the stack, pop the stack and update the answer list with the waiting days.
# Push the current day index onto the stack, and return the answer list after the loop.


# Complexity
# Time Complexity: O(n). Each element is pushed to and popped from the stack at most once, so the total number of operations is linear in the length of the temperatures list.
# Space Complexity: O(n). In the worst case (e.g., temperatures are strictly decreasing), the stack will store all indices, requiring linear extra space.
