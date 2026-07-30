class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
# 在旋转有序数组上用二分查找找最小值：
# 每次取中间值和右端点比较：
# 若中间值大于右端点，说明最小值在右半部分，移动左边界；
# 否则最小值在左半部分（含中间值），移动右边界。
# 循环结束时 left == right，指向的就是数组最小值。
# Use binary search on the rotated sorted array to find the minimum element:
# Compare the middle element with the right endpoint each time:
# If the middle element is greater than the right endpoint, the minimum lies in the right half, so move the left pointer.
# Otherwise, the minimum lies in the left half (including the middle), so move the right pointer.
# When the loop ends, left == right and points to the minimum element.

# Complexity
# Time Complexity: O(log n) — The search space is halved in each iteration.
# Space Complexity: O(1) — Only constant extra space is used.
