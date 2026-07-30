class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                height = heights[idx]
                width = i - stack[-1] - 1
                maxarea = max(maxarea, height * width)
            stack.append(i)
        return maxarea

# 用一个栈存柱子下标，保持栈里柱子越来越高。遇到矮柱子时，弹出栈顶的高柱子算它能围的面积；前后补两个 0，把栈里所有柱子都算一遍，取最大的那个。
# Use a stack to keep track of bar indices, keeping them in increasing height order. When you hit a shorter bar, pop the taller ones and calculate their max possible area. Adding zeros at both ends ensures all bars are processed.

# Complexity:
# Time Complexity: O(n) — Each bar is pushed to and popped from the stack at most once, resulting in linear time complexity.
# Space Complexity: O(n) — The stack can hold up to n elements in the worst case, such as when all bars are in increasing order.
