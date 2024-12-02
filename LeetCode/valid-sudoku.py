from typing import List
from pprint import pprint
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pprint(board)
        validity = True
        transposed = [list(row) for row in zip(*board)]
        for n in board:
            while '.' in n:
                n.remove('.')
            #print(sorted(n))
            #print(sorted(list(set(n))), '\n')
            if sorted(n) != sorted(list(set(n))):
                validity = False

        for n in transposed:
            while '.' in n:
                n.remove('.')
            #print(sorted(n))
            #print(sorted(list(set(n))), '\n')
            if sorted(n) != sorted(list(set(n))):
                validity = False

        return validity

if __name__ == "__main__":
    solution  = Solution()
    board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    result = solution.isValidSudoku(board)
    print(result)
