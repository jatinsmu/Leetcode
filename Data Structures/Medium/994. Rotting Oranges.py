from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # rotten = []
        rotten = deque()  # using a queue here so that pop operations are of O(1) as compared to O(n) if using list
        fresh = 0
        total_time = 0

        # calculate all fresh oranges and store indices of all rotten oranges so that we can iterate on them using BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # rotten
                    rotten.append([r, c])
                elif grid[r][c] == 1:
                    # fresh
                    fresh += 1

        # edge case
        if fresh == 0:
            return 0

        # now start from first rotten orange
        while len(rotten) > 0 and fresh > 0:

            # check for all rotten oranges at current level, so use for loop to traverse on all current indices in queueu before incrementing time
            for i in range(len(rotten)):
                # current_rotten = rotten.pop(0) # take out from the front of queue # pop using list takes O(n) time, since all elements in a list have to shift left
                current_rotten = rotten.popleft()  # using a proper queue here since popleft() in deque ins O(1) time
                print(f"current_rotten: {current_rotten}")

                # see in all directons from current_rotten
                all_directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # to add to current indecies

                for direction in all_directions:

                    # break case
                    cr = current_rotten[0] + direction[0]
                    cl = current_rotten[1] + direction[1]

                    # if we are out of bounds or current orange is not fresh, then skip
                    if cr < 0 or cr >= rows or cl < 0 or cl >= cols or grid[cr][cl] != 1:
                        pass

                    elif grid[cr][cl] == 1:
                        # spoil it
                        fresh -= 1
                        grid[cr][cl] = 2
                        # add it to queue
                        rotten.append([cr, cl])
                        # print(f"spoiling: {cr,cl}")

            # now, we have traversed all rotten oranges currently in queue, means this level traversal is done.
            total_time += 1
            print(f"total_time: {total_time}")

        # in end
        if fresh == 0:
            return total_time
        else:
            return -1






