class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_str = 0
        char = {}
        n = len(s)
        for right in range(n):
            c = s[right]
            if c in char and char[c] >= left:
                left = char[c] + 1
            char[c] = right
            max_str = max(max_str, right - left + 1)
        return max_str

# 用右指针下标遍历字符串，字典记录每个字符上次出现的位置，维护无重复滑动窗口。
# 若当前字符在窗口内重复，直接移动左边界到重复字符下一位，同步更新最长子串长度。
# Traverse the string with a right index pointer, use a dictionary to record the last position of each character to maintain a duplicate-free sliding window.
# If the current character repeats inside the window, shift the left boundary to the position after the repeated character and update the maximum substring length.

# Complexity Analysis
# Time Complexity: O(n), n is the length of input string. We traverse the string one single time, all dictionary lookup and assignment operations cost constant time.
# Space Complexity: O(min(m, n)), m is the total number of distinct available characters. The dictionary only stores unique characters from input string.
