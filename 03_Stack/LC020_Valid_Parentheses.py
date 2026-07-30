class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = "({["
        for c in s:
            if c in left:
                stack.append(c)
            elif c == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif c == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif c == "}":
                if not stack or stack.pop() != "{":
                    return False
        return len(stack) == 0

# 用栈存储左括号，遇到右括号时弹出栈顶匹配，不匹配或栈空直接返回 False。
# 遍历结束后栈为空，说明所有括号都正确配对，返回 True。
# Use a stack to store left brackets. When encountering a right bracket, pop the top element for matching. If it doesn't match or the stack is empty, return False.
# After the iteration, if the stack is empty, all brackets are correctly paired, so return True.
# Time Complexity: O(n), where n is the length of the string. Each character is pushed and popped from the stack at most once.
# Space Complexity: O(n), for the stack storage. In the worst case (all characters are left brackets), we need to store all of them.
