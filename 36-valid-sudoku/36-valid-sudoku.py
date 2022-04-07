class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = [set() for i in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur_val = board[i][j]
                if cur_val != '.':
                    if cur_val not in rows[i]:
                        rows[i].add(cur_val)
                    else:
                        return False

                    if cur_val not in cols[j]:
                        cols[j].add(cur_val)
                    else:
                        return False

                    # find the box that the position located

                    box_position = (i // 3) * 3 + j // 3

                    if cur_val not in boxs[box_position]:
                        boxs[box_position].add(cur_val)
                    else:
                        return False
        
        return True
        