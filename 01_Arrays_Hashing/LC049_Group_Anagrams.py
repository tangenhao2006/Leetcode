class Solution(object):
    # def is_anagrams(self,s,t):
    #     if len(s) != len(t):
    #         return False

    #     count = {}
    #     for char in s:
    #         if char not in count:
    #             count[char] = 1
    #         else:
    #             count[char] += 1

    #     for char in t:
    #         if char not in count:
    #             return False
    #         count[char] -= 1
    #         if count[char] < 0:
    #             return False

    #     return True

    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     if len(strs) == 1:
    #         return [strs]

    #     groups = []
    #     grouped = []
    #     n = len(strs)
    #     for i in range(n):
    #         s = strs[i]
    #         if s in grouped:
    #             continue

    #         current_group = [s]
    #         grouped.append(s)
    #         for j in range(i+1,n):
    #             t = strs[j]
    #             if self.is_anagrams(s,t):
    #                 current_group.append(t)
    #                 grouped.append(t)

    #         groups.append(current_group)
    #     return groups
    # 对每个字符串按字母排序生成唯一签名，用字典按签名分组，相同签名的字符串即为变位词。
    # Sort each string to generate a unique signature, then group strings by this signature using a dictionary.

    # Complexity：
    # Time Complexity: O(n⋅klogk)，其中 n 是字符串数量，k 是字符串平均长度，排序耗时为 O(klogk)。
    # Space Complexity: O(n⋅k)，用于存储所有字符串及其分组。
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())
