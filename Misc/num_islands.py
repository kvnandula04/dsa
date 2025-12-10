from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(i, j):
            nodes_to_visit = []
            visited.add((i, j))
            nodes_to_visit.append((i, j))

            while nodes_to_visit:
                x, y = nodes_to_visit.pop(0)
                directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]

                for dx, dy in directions:
                    i, j = x + dx, y + dy
                    if (
                        (i in range(rows))
                        and j in range(columns)
                        and grid[i][j] == "1"
                        and (i, j) not in visited
                    ):  # if the neighbouring cells are within bounds, are 1(land) and have not been previously visited, add the current node to be visited
                        nodes_to_visit.append((i, j))
                        visited.add((i, j))

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands


# Test code
sol = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(sol.numIslands(grid))  # Output: 1

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(sol.numIslands(grid))  # Output: 3
