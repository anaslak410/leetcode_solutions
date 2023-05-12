from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoks = {}
        for x in range(len(board)):
            for y in range(len(board)):

                cell = board[x][y]
                print(sudoks)
                if cell == '.':
                    continue
                elif cell in sudoks:
                    cell2 = sudoks[cell]
                    print("found in cell")
                    # print(cell2[0], cell[0])
                    if cell2[0] == cell[0]:
                        return False
                else:
                    # print("no")
                    sudoks[cell] = (x, y)


if __name__ == "__main__":
    sol = Solution()
    sol.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", "5", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
                      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
