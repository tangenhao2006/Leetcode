class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
# 旋转有序数组一定有一半区间是有序的，二分先判断左 / 右哪一侧有序，再看目标值是否落在有序区间内，不断缩小搜索范围找到目标索引。
# One half of the rotated sorted array must be sorted. Judge which half is ordered each time, check if the target lies in this ordered range, and narrow the search scope with binary search.

# complexity
# Time Complexity：O(log n)
# Space Complexity：O(1)
