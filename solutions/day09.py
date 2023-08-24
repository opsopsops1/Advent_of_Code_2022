# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-26 16:48:06
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-06 18:31:16
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    return self.simulate(data, 2)

  def part2(self, data):
    return self.simulate(data, 10)
  
  def simulate(self, data, knot_num):
    direct = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    knots = [(0, 0) for _ in range(knot_num)]
    visited = set([knots[-1]])

    for line in data:
      _dir, n = line.split(" ")
      for step in range(int(n)):
        knots[0] = (knots[0][0] + direct[_dir][0], knots[0][1] + direct[_dir][1])
        for k in range(knot_num-1):
          dx = knots[k][0] - knots[k+1][0]
          dy = knots[k][1] - knots[k+1][1]
          ch_x, ch_y = 0, 0
          if abs(dx) == 2 or abs(dy) == 2:
            ch_x = 0 if dx == 0 else 1 if dx > 0 else -1
            ch_y = 0 if dy == 0 else 1 if dy > 0 else -1
          if ch_x or ch_y:
            knots[k+1] = (knots[k+1][0]+ch_x, knots[k+1][1]+ch_y)
        visited.add(knots[-1])

    return len(visited)