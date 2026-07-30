class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        n = len(s)
        max_count = 0
        result = 0
        for right in range(n):
            char = s[right]
            if char not in count:
                 count[char] = 0
            count[char] += 1
            max_count = max(max_count, count[char])
            window_length = right - left + 1
            if window_length - max_count > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

# 双指针滑动窗口遍历字符串，字典统计窗口字符频次，实时记录窗口内出现最多的字符数量。
# 若窗口内需替换字符超过 k，则右移左边界缩小窗口，持续更新合法窗口的最大长度。
# Traverse the string with two sliding window pointers, use a dictionary to count character frequency and track the maximum frequency of one single character inside the window.
# Shrink the left boundary when the number of characters to replace exceeds k, and keep updating the maximum length of valid window.

# Complexity Analysis
# Time Complexity: O(n), n is the length of input string. The right pointer traverses all characters once, the left pointer only moves forward without backtracking. All dictionary operations are constant O(1).
# Space Complexity: O(1). The input only contains 26 uppercase letters, so the dictionary stores at most 26 entries, fixed constant space independent of input size.
        # left = 0
        # max_count = 0
        # count = {}
        # result = 0
        # n = len(s)
        # for right in range(n):
        #     char = s[right]
        #     if char not in count:
        #         count[char] = 0
        #     count[char] += 1
        #     max_count = max(max_count, count[char])
        #     window_length = right - left + 1
        #     if window_length - max_count > k:
        #         left_char = s[left]
        #         count[left_char] -= 1
        #         left += 1
        #     result = max(result, right - left + 1)
        # return result
