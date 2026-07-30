class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        maxL = maxR = result = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > maxL:
                    maxL = height[left]
                else:
                    result += maxL - height[left]
                left += 1
            else:
                if height[right] > maxR:
                    maxR = height[right]
                else:
                    result += maxR - height[right]
                right -= 1
        return result

# 使用双指针分别从数组两端向内遍历，维护左右两侧的最大高度 maxL 和 maxR。
# 哪边的高度更小，就用该侧的最大高度计算当前位置的存水量（max - height[i]），并向内移动指针，最终累加得到总水量。

# Use two pointers to traverse the array from both ends inward, keeping track of the maximum height encountered from the left (maxL) and the right (maxR).
# Calculate the water trapped at the current position using the smaller of the two maximum heights, then move the corresponding pointer inward. Sum the total trapped water.


# Complexity
# Time Complexity: O(n), where n is the length of the height array. The two pointers traverse the array only once.
# Space Complexity: O(1), as we only use a constant amount of extra space for variables like pointers and max heights.
