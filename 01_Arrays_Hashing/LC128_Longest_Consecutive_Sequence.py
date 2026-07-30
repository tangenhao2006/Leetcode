# 遍历去重后的集合，仅从连续段起点统计长度，规避重复计算保证 O (n)。
# Iterate unique set items, calculate sequence length only from start to avoid redundant work.
# Complexity
# Time: O(n)
# Space: O(n)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_so_far = 0
        for num in num_set:
            if num -1 not in num_set:
                curr = num
                curr_length = 1
                while curr + 1 in num_set:
                    curr += 1
                    curr_length += 1
                max_so_far = max(max_so_far, curr_length)
        return max_so_far
