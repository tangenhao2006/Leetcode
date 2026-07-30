class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[]for _ in range(9)]
        columns = [[]for _ in range(9)]
        boxes = [[]for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                bid = (i//3)*3 + j//3
                if num in rows[i] or num in columns[j] or num in boxes[bid]:
                    return False
                rows[i].append(num)
                columns[j].append(num)
                boxes[bid].append(num)
        return True

# 使用三组列表分别存储每行、每列、每个 3×3 子九宫出现过的数字，遍历棋盘，遇到空白符.直接跳过；通过公式bid=(i//3)*3+j//3计算格子所属九宫编号，若当前数字在本行 / 本列 / 本九宫已存在则直接返回 False，全部遍历无重复返回 True。
# Three lists are created to record digits appearing in each row, column and 3×3 sub-box. Traverse the whole board, skip blank cell marked with '.'. Calculate sub-box index via bid=(i//3)*3+j//3. Return False immediately if duplicate exists in row/column/sub-box, otherwise return True after full traversal.
# Complexity
# Time Complexity: O(1)Board size is fixed as 9×9=81 cells, total loop count is constant.
# Space Complexity: O(1)Each list stores at most 9 numbers, maximum occupied space is fixed constant.
