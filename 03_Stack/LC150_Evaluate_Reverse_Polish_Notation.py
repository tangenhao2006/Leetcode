class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif t == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif t == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(t))
        return stack.pop()

# Use a stack. Push numbers onto it. When encountering an operator, pop two elements, compute a op b, and push the result back. Division truncates toward zero.
# Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)
