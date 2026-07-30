from collections import deque
class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     left = 0
    #     result = []
    #     maximum = -float(inf)
    #     for i in range(n-k + 1):
    #         maximum = max(nums[i:i+k])
    #         result.append(maximum)
    #     return result

# 遍历所有合法窗口起点，每次截取长度为 k 的连续子数组。
# 对每个窗口直接调用 max 取最大值，存入结果列表后返回。

# Iterate all valid starting indices of sliding windows, slice subarray with fixed length k each time.
# Calculate maximum value for each window and collect values into result list.

# Complexity (Brute Force)
# Time Complexity: O(n*k), n = length of nums. Each window of size k calls max() which scans k elements.
# Space Complexity: O(k) for temporary window slice.

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        n = len(nums)
        for right in range(n):
            while dq and nums[right] >= nums[dq[-1]]:
                dq.pop()
            dq.append(right)
            while dq[0] <= right - k:
                dq.popleft()
            if right >= k - 1:
                result.append(nums[dq[0]])
        return result
# 核心规律：
# 如果一个数字 A 在窗口里，右边出现更大的数字 B，那么只要 B 还在窗口里，A 永远不可能成为任何窗口的最大值，可以直接永久删掉 A。
# 我们用队列只保存「有机会成为窗口最大值」的下标，且队列里下标对应数值严格从左到右递减，保证队列最左边永远是当前窗口最大值。

# 单调递减双端队列优化解法，使用deque存储数组下标
# 遍历数组右边界，维护单调递减队列，提前淘汰不可能成为窗口最大值的元素
# 清理滑出窗口的队首下标，窗口长度达到k时取出队首数值作为当前窗口最大值存入结果

# Traverse array with right pointer, maintain monotonically decreasing deque storing indices,
# eliminate elements that can never be window maximum in advance.
# Remove out-of-window indices from deque front, collect front value as window maximum once window length reaches k.

# Complexity (Monotonic Deque Optimization)
# Time Complexity: O(n), n = length of nums. Each element is pushed and popped from deque at most once, all operations are linear.
# Space Complexity: O(k), the deque stores at most k indices at any time.
