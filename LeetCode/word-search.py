from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = None
        col = None
        possible = True
        while possible is not False:
            if row is None and col is None :
                for letter in word:
                    for col_i ,col in enumerate(board):
                        if letter in col:
                            row = col.index(letter)
                            col = col_i
                            word = word[:-1]
                        else:
                            possible = False
            else:

if __name__ == "__main__":
    solution = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "FART"
    result = solution.exist(board, word)
    print(result)
