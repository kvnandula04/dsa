from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Helper function for depth-first search (DFS)
        def dfs(r, c, index):
            # If we've found the entire word
            if index == len(word):
                return True

            # If out of bounds or the current cell doesn't match the letter
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False

            # Mark the current cell as visited by temporarily changing its value
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all possible directions: up, down, left, right
            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )

            # Backtrack by resetting the current cell
            board[r][c] = temp

            return found

        # Try to find the word starting from every cell in the board
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
