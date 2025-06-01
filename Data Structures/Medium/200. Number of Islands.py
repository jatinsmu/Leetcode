class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            # base case for stopping recursion
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                # means either the row or col are invalid (as out of grid is considered water) or the current place is itself water, return False. Beacuse it is not land
                return False

            # We reach here, mean it will definitely be land. Mark that positioin as visited in grid. Means mark it as water.. so that we dont count it twice
            grid[row][col] = '0'

            # Do search on all 4 directions from current place
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            # if still we are able to reach here, then the current one is part of an island
            return True

        # iterate on each row and col combination to check if they are part of any island or not
        total_islands = 0
        for row in range(rows):
            for col in range(cols):
                # means it is land, do dfs search. If it is true, means it is an island
                # do dfs search starting from current row and col
                if dfs(row, col):
                    total_islands += 1

        return total_islands
