class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        while start < end:
            result = numbers[start] + numbers[end]
            if result == target:
                return [start + 1, end + 1]
            elif result < target:
                start += 1
            elif result > target:
                end -= 1
# 利用数组升序，首尾双指针求和；和偏小左指针右移、偏大右指针左移，命中目标下标 + 1 返回。
# 思路
# Use two pointers on sorted array from two ends. Move left right if sum < target, move right left if sum > target, return indices + 1 when matched.
# Complexity
# Time: O(n)
# Space: O(1)
