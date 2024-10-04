# 36. Valid Sudoku

# Sol. 3
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for val in row:
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # Check 3x3 sub-boxes
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                seen = set()
                for row in range(row_start, row_start + 3):
                    for col in range(col_start, col_start + 3):
                        val = board[row][col]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True


# Sol. 2

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = defaultdict(set)
#         cols = defaultdict(set)
#         boxes = defaultdict(set)
        
        
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
                
#                 if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
#                     return False
                
#                 rows[r].add(board[r][c])
#                 cols[c].add(board[r][c])
#                 boxes[(r // 3, c // 3)].add(board[r][c])
#                 print(rows)
        
#         return True

# Sol. 1 
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:

#         return checkRow(board) and checkColumn(board) and check33Box(board)

        

# def checkRow(board: List[List[str]]) -> bool:
#     for row in board:
#         for element in row:
#             if element == ".":
#                 continue
#             if row.count(element) != 1:
#                 return False
#     return True

# def checkColumn(board: List[List[str]]) -> bool:
    
#     for i in range(0,9):
#         column_list = []
#         for j in range(0,9):
#             # print(column_list, board[j][i])
#             # print(column_list.count(board[j][i]))
#             if board[j][i] == ".":
#                 continue
#             elif column_list.count(board[j][i]) >= 1:
#                 return False
#             column_list.append(board[j][i])
#     return True
                    

# def check33Box(board: List[List[str]]) -> bool:
#     start_row = 0
#     start_col = 0
    

#     for start_row in range(0,9,3):
#         for start_col in range(0,9,3):
#             box_list = []
#             for row in range(start_row, start_row + 3):
#                 for col in range(start_col, start_col + 3):
#                     # print(start_row, start_col, row, col)
#                     # print(box_list)
#                     if board[row][col] == ".":
#                         continue
#                     elif box_list.count(board[row][col]) >= 1:
#                         return False
#                     box_list.append(board[row][col])
#     return True