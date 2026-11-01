class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # try to solve it using bitmap
        # but how to check the presence of a number?
        # to check the duplicates, XOR bitmap with the target number (in the form
        # of left shift), if
        # result is smaller, duplicate exists
        # also need to build bitmaps for each row, column and sub-box
        row_bitmaps = [0] * 9
        col_bitmaps = [0] * 9
        # also the sequence of bitmaps stored in this list need to be discussed
        # or how to get to the right map by calculating row and col nums
        subB_bitmaps = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

        for row in range(0, 9):
            for col in range(0, 9):
                val = board[row][col]
                cur_row_bitmap = row_bitmaps[row]
                cur_col_bitmap = col_bitmaps[col]
                cur_subB_bitmap = subB_bitmaps[row // 3][col // 3]
                toFill = 1
                match val:
                    case "1":
                        toFill <<= 0
                    case "2":
                        toFill <<= 1
                    case "3":
                        toFill <<= 2
                    case "4":
                        toFill <<= 3
                    case "5":
                        toFill <<= 4
                    case "6":
                        toFill <<= 5
                    case "7":
                        toFill <<= 6
                    case "8":
                        toFill <<= 7
                    case "9":
                        toFill <<= 8
                    case ".":
                        continue

                new_row_bitmap = cur_row_bitmap ^ toFill
                if new_row_bitmap < cur_row_bitmap:
                    return False
                else:
                    row_bitmaps[row] = new_row_bitmap

                new_col_bitmap = cur_col_bitmap ^ toFill
                if new_col_bitmap < cur_col_bitmap:
                    return False
                else:
                    col_bitmaps[col] = new_col_bitmap

                new_subB_bitmap = cur_subB_bitmap ^ toFill
                if new_subB_bitmap < cur_subB_bitmap:                
                    return False
                else:
                    subB_bitmaps[row // 3][col // 3] = new_subB_bitmap
        
        return True
