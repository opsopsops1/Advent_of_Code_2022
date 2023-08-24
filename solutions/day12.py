# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-27 23:05:25
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-28 14:19:01
from utils.solution_base import SolutionBase
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

class Solution(SolutionBase):
  def part1(self, data):
    height_map, (sx, sy), (tx, ty), list_a = self.get_height_map(data)
    h, w = len(height_map), len(height_map[0])
    
    step = [[-1 for j in range(w)] for i in range(h)]
    step[sx][sy] = 0
    q = deque([(sx, sy)])
    while len(q):
      x, y = q.popleft()
      for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
          continue
        if step[nx][ny] == -1 and ord(height_map[nx][ny]) <= ord(height_map[x][y])+1:
          step[nx][ny] = step[x][y] + 1
          q.append((nx, ny))

    return step[tx][ty]

  def part2(self, data):
    height_map, (sx, sy), (tx, ty), list_a = self.get_height_map(data)
    h, w = len(height_map), len(height_map[0])

    step = [[-1 for j in range(w)] for i in range(h)]
    step[tx][ty] = 0
    q = deque([(tx, ty)])
    while len(q):
      x, y = q.popleft()
      for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
          continue
        if step[nx][ny] == -1 and ord(height_map[nx][ny]) >= ord(height_map[x][y])-1:
          step[nx][ny] = step[x][y] + 1
          q.append((nx, ny))
    ans = h*w
    for x, y in list_a:
      if step[x][y] != -1 and step[x][y] < ans:
        ans = step[x][y]
    return ans
  
  def get_height_map(self, data):
    h, w = len(data), len(data[0])
    height_map = data[::]
    list_a = []
    for i in range(h):
      for j in range(w):
        if height_map[i][j] == "S":
          sx, sy = i, j
          height_map[i] = height_map[i].replace("S", "a")
        if height_map[i][j] == "E":
          tx, ty = i, j
          height_map[i] = height_map[i].replace("E", "z")
        if height_map[i][j] == "a":
          list_a.append((i, j))

    return height_map, (sx, sy), (tx, ty), list_a
  