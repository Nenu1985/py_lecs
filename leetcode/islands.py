# https://leetcode.com/problems/number-of-islands/
from typing import List

from collections import deque


class Solution:
    def bfs(self, row, col):
      N = len(self.grid)
      M = len(self.grid[0])
      # left/right; down/up
      directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
      queue = deque()
      queue.append((row, col))
      while queue:
        x, y = queue.popleft()
        self.grid[x][y] = "0"
        for dx, dy in directions:
          nx = dx + x
          ny = dy + y
          if 0 <= nx < N and 0 <= ny < M and self.grid[nx][ny] == "1":
            queue.append((nx, ny))
            self.grid[nx][ny] = "0"
          
    def numIslands(self, grid: List[List[str]]) -> int:
      self.grid = grid
      N = len(grid)
      M = len(grid[0])
      count = 0
      for row in range(N):
        for col in range(M):
          if self.grid[row][col] == "1":
            count += 1
            self.bfs(row, col)
      return count

s = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid))