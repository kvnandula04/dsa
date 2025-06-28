from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        starting_colour = image[sr][sc]

        if starting_colour == color:
            return image
        
        def dfs(r, c):
            # base case
            if (r < 0 or r > len(image) or c < 0 or c > len(image[0]) or image[r][c] != starting_colour):
                return
            
            # modify the colour
            image[r][c] = color

            # recursive case
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right

        dfs(sr, sc)
        return image