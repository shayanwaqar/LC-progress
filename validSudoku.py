class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            rset = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rset:
                    return False
                rset.add(board[r][c])
        
        for c in range(cols):
            cset = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c] in cset:
                    return False
                cset.add(board[r][c])


        for r in range(0, rows, 3):
            for c in range(0, cols, 3):
                bset = set()
                for br in range(r, r+3):
                    for bc in range(c, c+3):
                        element = board[br][bc]
                        if element == ".":
                            continue
                        if element in bset:
                            return False
                        else:
                            bset.add(element)
        return True