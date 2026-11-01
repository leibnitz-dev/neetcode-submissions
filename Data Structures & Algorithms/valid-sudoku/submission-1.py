class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row wise check 
        flag_row = 0
        for row in board:
            seen = set()
            for v in row:
                if v == '.':
                    continue
                if v in seen:
                    flag_row = 1
                    break
                seen.add(v)
            if flag_row == 1:
                break
        if flag_row == 1:
            return False
        # column wise check 
        flag_col = 0
        for it in range(len(board[0])):
            column = []
            seen = set()
            for row_cnt in range(9):
                column.append(board[row_cnt][it])
            for v in column:
                if v == '.':
                    continue
                if v in seen:
                    flag_col = 1
                    break
                seen.add(v)
            if flag_col == 1:
                break 
        if flag_col == 1:
            return False

        # box wise check
        boxes = []
        
        for i in range(0, len(board), 3):
            sub_boxes = [[],[],[]]
            section = board[i:i+3]
            span = 3
            for sub_rows in section:
                cnt = 0
                for idx in range(0, 9, 3):
                    for v in sub_rows[idx: idx+span]:
                        sub_boxes[cnt].append(v)
                    cnt+= 1
            for row in sub_boxes:
                boxes.append(row)
        
        flag_box = 0
        for box in boxes:
            seen = set()
            for v in box:
                if v == ".":
                    continue
                if v in seen:
                    flag_box = 1
                    break 
                seen.add(v)
                if flag_box== 1:
                    break 
            if flag_box == 1:
                break 
        if flag_box == 1:
            return False
        
        return True

            


       



    

        

            



        


            
        