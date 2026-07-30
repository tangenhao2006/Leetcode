class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = {}
        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        n = len(s)
        left = 0
        min_len = float("inf")
        window = {}
        matched = 0
        start_idx = 0

        for right in range(n):
            char = s[right]
            if char not in window:
                window[char] = 0
            window[char] += 1

            if char in need and window[char] == need[char]:
                matched += 1
            while matched == len(need):
                current_min_len = right - left + 1
                if current_min_len < min_len:
                    min_len = current_min_len
                    start_idx = left
                left_char = s[left]
                if left_char in need and window[left_char] == need[left_char]:
                    matched -= 1
                window[left_char] -= 1
                left += 1
        if min_len == float("inf"):
            return ""
        return s[start_idx : start_idx + min_len]

# 字典统计 t 所需字符数量，右指针扩张窗口并统计窗口字符，字符数量达标则匹配种类 + 1。
# 窗口覆盖全部目标字符时收缩左边界，更新最短窗口起止下标，最终截取最短子串或返回空串。
# Count required character frequency of t with a dictionary, expand window via right pointer and increase matched types when character count meets demand.
# Shrink left pointer when window contains all target characters, record the shortest window index, slice substring or return empty string as result.

# Complexity
# Time Complexity: O(m + n), m = len(t), n = len(s). Each character is processed at most twice by left/right pointers, dict operations are O(1).
# Space Complexity: O(k), k = distinct characters in t, only limited fixed storage for two dictionaries.
