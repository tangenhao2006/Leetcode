class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours_need = 0
            for pile in piles:
                hours_need += math.ceil(pile / mid)
            if hours_need <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left

# 在 [1, max(piles)] 区间上二分查找最小速度，每次计算以当前速度吃完所有香蕉的总耗时，不断缩小范围找到满足条件的最小值。
# Binary search on the speed range [1, max(piles)]. Calculate the total hours needed for the current speed and narrow the range to find the minimum feasible speed.

# Complexity
# Time Complexity: O(n log(max(piles))) — Each binary search step takes O(n) to compute total hours, and there are O(log(max(piles))) steps.
# Space Complexity: O(1) — Only constant extra space is used.
