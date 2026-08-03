class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit = set()
        islands = 0
        def bfs(r,c): 
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if (new_row in range(len(grid)) and
                    (new_col in range(len(grid[0]))) and 
                    grid[new_row][new_col] == '1' and
                    (new_row,new_col) not in visit):
                        q.append((new_row,new_col))
                        visit.add((new_row,new_col))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i,j) not in visit:
                    bfs(i,j)
                    islands += 1
        return islands

