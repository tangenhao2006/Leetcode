class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 用字典记录遍历过的数字及其下标，对每个数计算差值 target - n，若差值已在字典中则返回两个下标，否则存入当前数和下标。
    # Use a hash map to store seen numbers and their indices. For each number n, check if target - n exists in the map;
    # if yes, return the two indices; else add n and its index to the map.
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in dict:
                return [dict[diff], i]

            dict[num] = i
