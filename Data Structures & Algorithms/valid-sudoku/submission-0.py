class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_box_index(row, column):
            if 0<=row<=2:
                return (column//3)
            elif 3<=row<=5:
                return 3+(column//3)
            elif 6<=row<=8:
                return 6+(column//3)
        row_list = [set() for _ in range(9)]
        col_list = [set() for _ in range(9)]
        box_list = [set() for _ in range(9)]
        for i in range(len(board)): #i-row and j-column
            for j in range(len(board[i])):
                if board[i][j]!=".":
                    val = board[i][j]
                    if val in row_list[i] or val in col_list[j] or val in box_list[get_box_index(i,j)]:
                        return False
                    else:
                        row_list[i].add(val)
                        col_list[j].add(val)
                        box_list[get_box_index(i,j)].add(val)

        return True
        