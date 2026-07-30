class Solution(object):
    # def containsDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if nums[i] == nums[j]:
    #                 return True
    #     return False
# 排序后相邻检查
# 先对数组排序，再遍历检查相邻元素是否相等，相等则返回 True。
# Sort the array first, then check adjacent elements for equality.
# 集合长度对比
# 将数组转为集合自动去重，比较原数组和集合的长度，不等则说明有重复。
# Convert the list to a set to remove duplicates; if lengths differ, duplicates exist.

    # def containsDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     nums.sort()
    #     for i in range(1,len(nums)):
    #         if nums[i] == nums[i-1]:
    #             return True
    #     return False

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
