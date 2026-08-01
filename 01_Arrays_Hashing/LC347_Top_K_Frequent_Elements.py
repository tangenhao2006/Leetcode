class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        pairs = []
        for num in dict:
            pairs.append([dict[num], num])
        pairs.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(pairs[i][1])

        return res
# 先用字典统计每个数字的出现次数，再将（次数，数字）配对为列表，按次数降序排序，最后取前 k 个数字作为结果。
#  Use a dictionary to count the frequency of each number, pair each (frequency, number) into a list, sort the list in
#  descending order by frequency, and return the first k numbers.

# Complexity
# Time Complexity: O(nlogn)
# Counting frequencies: O(n)
# Sorting the list of pairs: O(mlogm), where m is the number of unique elements (at most n).
# Space Complexity: O(n)
# The dictionary stores at most n unique elements, and the pairs list also takes O(n) space.
