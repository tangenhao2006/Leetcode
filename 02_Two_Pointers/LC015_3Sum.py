class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum_so_far = nums[i] + nums[j] + nums[k]
                if sum_so_far == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum_so_far > 0:
                    k -= 1
                else:
                    j += 1
        return result

# 数组排序，固定 i 并跳过重复，双指针 j、k 查找；命中答案后左右指针各自跳过连续重复元素，原生去重不用 set 提速。
# Sort array, fix i and skip duplicates, use two pointers j&k; skip repeated values after matching triplet to deduplicate without set.
# Complexity
# Time: O(n2)
# Space: O(logn)
