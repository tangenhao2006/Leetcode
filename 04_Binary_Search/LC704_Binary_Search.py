class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# 在有序数组中，每次取中间位置和目标值比较，根据大小关系缩小一半搜索范围，直到找到目标或搜索区间为空。
# In a sorted array, repeatedly compare the middle element with the target and narrow the search range by half until the target is found or the range is empty.

# Complexity:
# Time Complexity: O(log n) — The search space is halved in each iteration.
# Space Complexity: O(1) — Constant extra space is used.
