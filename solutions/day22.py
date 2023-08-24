# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-07 19:25:57
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-12 23:07:37
from utils.solution_base import SolutionBase
import re

facing = [">", "v", "<", "^"]
facing_v = {">": 0, "v": 1, "<": 2, "^": 3}

class Solution(SolutionBase):
  def part1(self, data):
    board, path = self.parse_data(data)
    h, w = len(board), len(board[0])

    boundary_row, boundary_col = [], []
    for i in range(h):
      l = 0
      for j in range(w):
        if board[i][j] != " ":
          l = j
          break
      for j in range(w-1, -1, -1):
        if board[i][j] != " ":
          boundary_row.append((l, j))
          break
    for j in range(w):
      u = 0
      for i in range(h):
        if board[i][j] != " ":
          u = i
          break
      for i in range(h-1, -1, -1):
        if board[i][j] != " ":
          boundary_col.append((u, i))
          break

    start = (0, boundary_row[0][0])

    regex = re.compile(r"(\d+[LR]?)")
    path_step = regex.findall(path)
    # print(sum(int(s[:]) if s.isdigit() else int(s[:-1]) for s in path_step))

    now_pos = start
    now_fac = 0

    for step in path_step:
      step_num, turn = (int(step), " ") if step.isdigit() else (int(step[:-1]), step[-1])

      for _ in range(step_num):
        match now_fac:
          case 0:
            new_i, new_j = (now_pos[0], now_pos[1]+1)
            if new_j > boundary_row[new_i][1]:
              new_j = boundary_row[new_i][0]
          case 1:
            new_i, new_j = (now_pos[0]+1, now_pos[1])
            if new_i > boundary_col[new_j][1]:
              new_i = boundary_col[new_j][0]
          case 2:
            new_i, new_j = (now_pos[0], now_pos[1]-1)
            if new_j < boundary_row[new_i][0]:
              new_j = boundary_row[new_i][1]
          case _:
            new_i, new_j = (now_pos[0]-1, now_pos[1])
            if new_i < boundary_col[new_j][0]:
              new_i = boundary_col[new_j][1]
        if board[new_i][new_j] == "#":
          break
        else:
          now_pos = (new_i, new_j)

      if turn == "R":
        now_fac = (now_fac+1)%4
      elif turn == "L":
        now_fac = (now_fac+3)%4
    
    return 1000*(now_pos[0]+1) + 4*(now_pos[1]+1) + facing_v[facing[now_fac]]

  # def part2(self, data):
  #   if len(data) > 10:
  #     return "Testing"
  #   board, path = self.parse_data(data)
  #   h, w = len(board), len(board[0])

  #   return "Test"

  def parse_data(self, data):
    board, path = "\n".join(data).split("\n\n")
    board = board.split("\n")
    h, w = len(board), max(len(line) for line in board)
    for i, line in enumerate(board):
      new_line = line.ljust(w, " ")
      board[i] = new_line

    return board, path
