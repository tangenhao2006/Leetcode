class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            answer[i] *= right
            right *= nums[i]
        return answer


# 先正序遍历存储各位置左侧乘积，逆序遍历用变量维护右侧乘积，二者相乘得到结果。
# Traverse forward to store left product, then backward to multiply with maintained right product for final answer.
# Complexity
# Time Complexity: O(n)
# Space Complexity: O(1)
# [1,2,3,4] -> left: [1,1,2,6]. expect:[24,12,8,6]
