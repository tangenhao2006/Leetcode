class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            h = min(height[left],height[right])
            result = max(result, width * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
# 左右指针从两端向内遍历，容器容积 = 矮柱高度 × 间距，矮柱对应指针向内移动，持续更新最大容积。
# Two pointers start from both ends. Area = shorter height × width, move the shorter-side pointer and keep updating max area.
# Complexity
# Time: O(n)
# Space: O(1)
