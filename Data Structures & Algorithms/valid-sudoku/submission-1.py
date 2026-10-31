class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # do it in the brute force first to find some insights
        keys = ["1","2","3","4","5","6","7","8","9","."]
        stat = dict.fromkeys(keys, 0)
        # traverse the rows first
        for row in board:
            for value in row:
                stat[value] += 1
            for key, value in stat.items():
                if value > 1 and key != ".":
                    return False
            stat = dict.fromkeys(keys, 0)

        # traverse the columns
        for col in range (0, 9):
            for row in board:
                stat[row[col]] += 1
            for key, value in stat.items():
                if value > 1 and key != ".":
                    return False
            stat = dict.fromkeys(keys, 0)

        # traverse the sub-boxes
        for row_offset in range(0, 9, 3):
            for col_offset in range(0, 9, 3):
                for row_num in range(0, 3):
                    for col_num in range(0, 3):
                        stat[board[row_num + row_offset][col_num + col_offset]] += 1
                for key, value in stat.items():
                    if value > 1 and key != ".":
                        return False
                stat = dict.fromkeys(keys, 0)

        return True