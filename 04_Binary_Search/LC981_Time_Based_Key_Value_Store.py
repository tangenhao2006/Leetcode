class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = [[], []]
        self.data[key][0].append(value)
        self.data[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        value_list, time_list = self.data[key]
        left = 0
        right = len(time_list) - 1
        best_index = -1
        while left <= right:
            mid = (left + right) // 2
            if time_list[mid] <= timestamp:
                best_index = mid
                left = mid + 1
            else:
                right = mid - 1
        if best_index == -1:
            return ""
        return value_list[best_index]

# 采用字典存储，每个键对应值列表与升序时间戳列表；查询时手写二分查找不大于目标时间戳的最大合法下标，返回对应值，无有效数据则返回空字符串。
# We use a dictionary to store data, each key maps to a value list and an ascending timestamp list. Binary search is implemented to find the largest valid index whose timestamp is no larger than the target timestamp, then return the matched value or an empty string if no valid record exists.

# Complexity
# Time Complexity: O(1) for set operation, O(log n) for each get binary search.
# Space Complexity: O(n), where n is the total number of stored key-timestamp-value records


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# "foo" : [[1,4], ["bar","bar2"]]
