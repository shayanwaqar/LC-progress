class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        oranges = False
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:#rotten orange found
                    q.append((r,c))
                if grid[r][c] == 1:
                    oranges = True
        
        # if not oranges:
        #     return -1

        if len(q) == 0: #no oranges in the grid
            return 0 if not oranges else -1
        
        #now q contains all rotten oranges
        level = -1 #might have to start at 1
        while q:
            level += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]
                for dr, dc in directions:
                    if dr < 0 or dr == rows or dc < 0 or dc == cols or grid[dr][dc] == 2:
                        continue
                    if grid[dr][dc] == 1:
                        grid[dr][dc] = 2 #mark as rotten
                        q.append((dr,dc)) #then append it to the q
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:#normal orange found
                    return -1

        return level
                        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # rows = len(grid)
        # cols = len(grid[0])

        # q = deque()
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 2:
        #             q.append((r,c, 0))
        
        # #bfs
        # ret = 0
        # while q:
        #     r,c,t = q.popleft()
        #     ret = max(ret, t)
        #     directions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
        #     for dr, dc in directions:
        #         if dr < 0 or dr == rows or dc < 0 or dc == cols or grid[dr][dc] == 0 or grid[dr][dc] == 2:
        #             continue
        #         grid[dr][dc] = 2 #mark as visited
        #         q.append((dr,dc,t+1))
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             return -1

        # return ret
        