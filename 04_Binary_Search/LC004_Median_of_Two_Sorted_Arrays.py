class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        left_total = (m+n+1) // 2
        while left < right:
            i = (left + right + 1) // 2
            j = left_total - i
            # i + j = left_total
            # 从 nums1 的左侧选取 i 个元素，放在合并后数组的左半部分
            # 从 nums2 的左侧选取 j 个元素，放在合并后数组的左半部分
            if nums1[i -1] > nums2[j]:
                right = i - 1
            else:
                left = i
        i , j = left, left_total - left
        maxleft1 = nums1[i-1] if i > 0 else float('-inf')
        maxleft2 = nums2[j-1] if j > 0 else float('-inf')
        minright1 = nums1[i] if i < m else float('inf')
        minright2 = nums2[j] if j < n else float('inf')

        if (m + n) % 2 == 1:
            return max(maxleft1, maxleft2)
        else:
            return (max(maxleft1,maxleft2) + min(minright1, minright2))/2

# 数组交换优化：确保 nums1 是长度更短的数组，仅在短数组上做二分查找，最小化二分迭代次数，时间复杂度优化为 O(log(min(m,n)))。
# 定义分割规则：设两个数组总长度为 m+n，left_total = (m+n+1)//2，规定合并后左半区间一共存放 left_total 个元素，该公式可以统一处理总长度奇数、偶数两种场景。
# 二分寻找合法分割点：
# 在 nums1 的区间 [0,m] 二分，i 代表从 nums1 左侧选取 i 个元素放入左半区；由 i+j=left_total 推出 j，即从 nums2 左侧选取 j 个元素放入左半区。
# 若 nums1 左半区间最大值大于 nums2 右半区间最小值，说明 nums1 分割位置太靠右，需要向左收缩边界；反之向右试探寻找更大的合法分割位置。
# 边界值处理：用正负无穷分别处理某一侧没有元素的越界场景，计算左半区间整体最大值、右半区间整体最小值。
# 计算中位数：总长度为奇数时，左半区间最大值即为中位数；总长度为偶数时，取左半最大值与右半最小值的平均值作为中位数。

# Swap two arrays to guarantee nums1 is the shorter one, so we only perform binary search on the shorter array to reduce search times.
# Calculate left_total = (m+n+1)//2 to fix the total number of elements on the left partition of the merged array, which unifies the logic for odd and even total lengths.
# Use binary search to find the valid split index i in nums1, and j is determined by i + j = left_total. Adjust the binary search boundary to ensure all elements on the left partition are less than or equal to elements on the right partition.
# Use positive and negative infinity to handle edge cases where one partition has no elements, then get the maximum value of the left partition and the minimum value of the right partition.
# Return the left maximum if the total length is odd; otherwise return the average of left maximum and right minimum as the median.


# Complexity
# Time Complexity: O(log(min(m,n)))
# Space Complexity: O(1)


        # [1,3,5,6]
        # [2,4,7,8]
        # [1,2,3,4,5,6,7,8] -> 4.5
