class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        stack = []
        for pos, speed in cars:
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

# 车辆按位置降序排列，用栈维护车队：后车耗时大于前车时形成新车队，否则合并。栈的长度就是车队总数。
# Approach (English)
# Sort cars by position descending. Use a stack: if a car's time is greater than the stack top, push it (new fleet). The stack size is the answer.
# Complexity
# Time Complexity: O(n log n)
# Space Complexity: O(n)
