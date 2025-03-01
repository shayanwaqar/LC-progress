class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        grid = mat #variable name, same ref in memory
        rows = len(grid)
        cols = len(grid[0])

        vset = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))
                    vset.add((r,c))
        
        while q:
            r,c,d = q.popleft()
            directions = [(r-1,c), (r,c-1), (r+1,c), (r,c+1)]
            for dr, dc in directions:
                if dr < 0 or dc < 0 or dr == rows or dc == cols or (dr,dc) in vset:
                    continue
                grid[dr][dc] = d + 1
                q.append((dr,dc,d+1)) #append with incremented distance
                vset.add((dr,dc))
        
        return grid



# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         grid = mat #variable name, same ref in memory
#         rows = len(grid)
#         cols = len(grid[0])

#         vset = set()
#         q = deque()
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] != 0:
#                     grid[r][c] = -1 #marking as unprocessed
#                 if grid[r][c] == 0:
#                     q.append((r,c))
#                     vset.add((r,c))
        
#         while q:
#             r,c = q.popleft()
#             directions = [(r-1,c), (r,c-1), (r+1,c), (r,c+1)]
#             for dr, dc in directions:
#                 if dr < 0 or dc < 0 or dr == rows or dc == cols or (dr,dc) in vset: 
#                     continue
#                 if grid[dr][dc] == -1:
#                     q.append((dr,dc))  
#                     grid[dr][dc] = grid[r][c] + 1
#                     vset.add((r,c))
        
#         return grid