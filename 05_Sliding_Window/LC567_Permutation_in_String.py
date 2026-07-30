class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        len1 = len(s1)
        len2 = len(s2)
        count1 = {}
        for c in s1:
            if c not in count1:
                count1[c] = 0
            count1[c] += 1
        window =  {}
        for i in range(len1):
            char = s2[i]
            if char not in window:
                window[char] = 0
            window[char] += 1
        if window == count1:
            return True
        for right in range(len1, len2):
            left_char = s2[right - len1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            char = s2[right]
            if char not in window:
                window[char] = 0
            window[char] += 1
            if window == count1:
                return True
        return False

# 统计 s1 所有字符出现次数，先构建 s2 第一段和 s1 等长的窗口并统计窗口字符。
# 滑动窗口时移除最左侧字符、新增右侧字符，每次对比窗口与 s1 的频次字典，匹配则返回 True。
# Count the frequency of each character in s1, initialize the first fixed-length window on s2 and record character frequency inside the window.
# Remove the leftmost character and add new right character when sliding window, compare two frequency dictionaries each iteration and return True if they match exactly.

# Complexity Analysis
# Time Complexity: O(n + m), n is length of s1, m is length of s2. We traverse s1 and s2 once separately. Comparing two dictionaries only checks at most 26 lowercase letters, which counts as constant O(1).
# Space Complexity: O(1). Input only contains 26 lowercase letters, so two dictionaries store at most 26 entries, memory usage is fixed and independent of input length
