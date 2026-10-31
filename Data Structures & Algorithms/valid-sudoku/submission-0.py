class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # do it in the brute force first to find some insights
        keys = ["1","2","3","4","5","6","7","8","9","."]
        row_stat = dict.fromkeys(keys, 0)
        col_stat = dict.fromkeys(keys, 0)
        subB_stat = dict.fromkeys(keys, 0)

        # traverse the rows first
        for row in board:
            for value in row:
                row_stat[value] += 1
            for key, value in row_stat.items():
                if value > 1 and key != ".":
                    return False
            row_stat = dict.fromkeys(keys, 0)

        # traverse the columns
        for col in range (0, 9):
            for row in board:
                col_stat[row[col]] += 1
            for key, value in col_stat.items():
                if value > 1 and key != ".":
                    return False
            col_stat = dict.fromkeys(keys, 0)

        # traverse the sub-boxes
        for row_offset in range(0, 9, 3):
            for col_offset in range(0, 9, 3):
                for row_num in range(0, 3):
                    for col_num in range(0, 3):
                        subB_stat[board[row_num + row_offset][col_num + col_offset]] += 1
                for key, value in subB_stat.items():
                    if value > 1 and key != ".":
                        return False
                subB_stat = dict.fromkeys(keys, 0)

        return True