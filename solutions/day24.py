# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-12 01:39:08
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-12 13:11:27
from utils.solution_base import SolutionBase

dx = [0, 1, 0, -1, 0]
dy = [1, 0, -1, 0, 0]

class Solution(SolutionBase):
  def part1(self, data):
    h, w = len(data), len(data[0])
    start = (0, 1)
    target = (h-1, w-2)
    blizzard_row, blizzard_col = self.parse_data(data)

    q = set()
    q.add((start, 0))

    while q:
      new_q = set()

      for (x, y), now_step in q:
        if (x, y) == target:
          return now_step

        next_step = now_step + 1

        for d in range(5):
          nx = x + dx[d]
          ny = y + dy[d]

          # Over boundary
          if nx < 0 or nx >= h or data[nx][ny] == "#":
            continue
          # In blizzard
          if (nx, ny) in blizzard_row[next_step%(w-2)] or (nx, ny) in blizzard_col[next_step%(h-2)]:
            continue
          
          # print(next_step)
          new_q.add(((nx, ny), next_step))

      q = new_q

  def part2(self, data):
    h, w = len(data), len(data[0])
    start = (0, 1)
    target = (h-1, w-2)
    blizzard_row, blizzard_col = self.parse_data(data)

    q = set()
    q.add((start, 0))
    goal = target
    his = []
    back = False

    while q:
      new_q = set()

      for (x, y), now_step in q:
        if (x, y) == goal:
          his.append(now_step)
          if len(his) == 3:
            return his[-1]

          if goal == target:
            goal = start
          else:
            goal = target

          back = True
          new_q.clear()

        next_step = now_step + 1

        for d in range(5):
          nx = x + dx[d]
          ny = y + dy[d]

          # Over boundary
          if nx < 0 or nx >= h or data[nx][ny] == "#":
            continue
          # In blizzard
          if (nx, ny) in blizzard_row[next_step%(w-2)] or (nx, ny) in blizzard_col[next_step%(h-2)]:
            continue
          
          # print(next_step)
          new_q.add(((nx, ny), next_step))

        if back:
          back = False
          break

      q = new_q

  def parse_data(self, data):
    h, w = len(data), len(data[0])

    blizzard_row = [set() for t in range(w-2)]
    blizzard_col = [set() for t in range(h-2)]
    motion = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

    for i, row in enumerate(data):
      for j, c in enumerate(row):
        if c == "#" or c == ".":
          continue
        mv = motion[c]
        if c == ">" or c == "<":
          for t in range(0, w-2):
            ni = (i-1+mv[0]*t+h-2)%(h-2)+1
            nj = (j-1+mv[1]*t+w-2)%(w-2)+1
            blizzard_row[t].add((ni, nj))
        elif c == "v" or c == "^":
          for t in range(0, h-2):
            ni = (i-1+mv[0]*t+h-2)%(h-2)+1
            nj = (j-1+mv[1]*t+w-2)%(w-2)+1
            blizzard_col[t].add((ni, nj))
            
    return blizzard_row, blizzard_col
