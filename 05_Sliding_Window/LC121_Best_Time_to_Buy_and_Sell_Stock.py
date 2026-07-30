class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            if price < min_price:
                min_price = price
        return max_profit

# 遍历股价数组，使用历史最低股价计算当日卖出可获得的利润，同步更新全局最大利润。
# 计算利润后再更新历史最低价，保证买入日期一定早于卖出日期，满足交易规则。

# Iterate through the price list, calculate daily profit based on the historical minimum price and update the global maximum profit value.
# Update the minimum price after profit calculation to guarantee the buy day occurs before the sell day.

# Complexity Analysis
# Time Complexity: O(n), n represents the total number of elements in the price array. We traverse the array exactly once, all operations inside the loop are constant-time comparisons and arithmetic calculations.
# Space Complexity: O(1). Only two fixed integer variables max_profit and min_price are created to store intermediate results; no auxiliary data structures that expand with input size are used.
