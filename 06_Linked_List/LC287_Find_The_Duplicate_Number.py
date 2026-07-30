class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


        # n + 1 integers with at most n values -> at least two same integers

# 建立下标i到nums[i]的映射，把数组模拟成带环链表，采用Floyd快慢指针两阶段求解重复数字
# 第一阶段慢指针单次映射、快指针两次映射前进，在环内相遇得到路程等量关系；
# 第二阶段重置慢指针至下标0，双指针同步单步映射移动，再次相遇点为环入口即重复值
# 仅读取数组不修改原数组，仅两个临时变量，满足常数O(1)空间限制

# Build mapping from index i to nums[i], simulate array as cyclic linked list with two-stage Floyd slow-fast pointer algorithm.
# Stage 1: slow moves one mapping, fast moves two mappings per loop to get their meeting point inside cycle for distance deduction.
# Stage 2: reset slow pointer to index 0, both pointers move one mapping each iteration; their second meeting point is cycle entry (duplicate number).
# Only read original array without modification, only two temp variables, constant O(1) extra space.

# Complexity
# Time Complexity: O(n), at most two linear traversals of array
# Space Complexity: O(1), only slow, fast temporary variables

# 关键数学结论
# 设：L = 起点 0 到环入口步数，C = 环周长，x = 环入口到快慢第一次相遇点步数快慢指针同时间相遇时路程满足：2(L+x)=L+kC+x化简得核心等式：L=kC−x文字结论：从数组起点走到环入口的步数 L，等于从第一次相遇点出发走 L 步后恰好抵达环入口。因此：第一次相遇后，将慢指针重置到下标 0，快慢指针同步每次走 1 步，再次相遇位置就是环入口，即数组重复数字。
# 二、两段代码作用总结

# 第一个 while slow != fast慢指针每次 1 步，快指针每次 2 步，利用速度差让二者在环内任意一点相遇；仅用来获取相遇点，建立路程等量关系，相遇点本身不是答案，不能直接 return。
# 第二个 while slow != fast慢指针重置回起点 0，快慢均单次一步同步前进；依据 L=kC−x，二者一定会在环入口重逢，该数值即为重复数字。

# 三、完整算法思路

# 建立下标 i 到 nums [i] 的映射，将数组模拟为带环链表，快慢指针以 1 步、2 步速度移动直至环内相遇；
# 重置慢指针至数组起点，两指针同步单步跳转，再次相遇的位置就是重复数字。

# Build index-to-value mapping to simulate array as a cyclic linked list. Slow pointer moves one step, fast moves two steps per iteration until they meet inside the cycle.
# Reset slow pointer to index 0, move both pointers one step each loop; their second meeting point is the duplicate number.

# Complexity
# Time Complexity: O(n)
# At most two full passes over the array, linear time relative to array length n.
# Space Complexity: O(1)
# Only two temporary variables slow and fast, no extra array/hash storage, constant extra space.
