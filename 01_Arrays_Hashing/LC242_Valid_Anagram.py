class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    # Check length first：长度不同直接返回 False，然后用哈希表统计 s 中字符出现次数，再遍历 t 抵消计数，异常则返回 False。
    # Count chars in s with a hash map, then decrement counts with chars in t; any mismatch means not an anagram.
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}

        for letter in s:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1

        for letter in t:
            if letter not in count:
                return False
            count[letter] -= 1
            if count[letter] < 0:
                return False

        return True
