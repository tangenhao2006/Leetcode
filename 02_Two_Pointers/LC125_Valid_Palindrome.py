class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                new_str += char.lower()

        return new_str == new_str[::-1]

# 用左右双指针从字符串两端向中间遍历，跳过非字母数字字符，将字符转为小写后对比，全部匹配则为回文。
#  Use two pointers starting from both ends, skip non-alphanumeric characters, compare characters in lowercase, and return true if all pairs match.

# Complexity
# Time Complexity: O(n)
# Space Complexity: O(1)
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
