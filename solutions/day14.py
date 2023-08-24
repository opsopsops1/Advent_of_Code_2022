# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-28 16:42:19
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-10 21:54:28
from utils.solution_base import SolutionBase

d = [(0, 1), (-1, 1), (1, 1)]

class Solution(SolutionBase):
  def part1(self, data):
    sand_pos = (500, 0)
    rocks = self.parse_data(data)
    sand = set()
    deepest = max([p[1] for p in rocks])

    while sand_pos[1] < deepest:
      for dx, dy in d:
        next_pos = (sand_pos[0] + dx, sand_pos[1] + dy)
        if next_pos not in rocks and next_pos not in sand:
          # sand drop
          sand_pos = next_pos
          break
      else:
        # sand not drop
        sand.add(sand_pos)
        sand_pos = (500, 0)

    return len(sand)

  def part2(self, data):
    sand_pos = (500, 0)
    rocks = self.parse_data(data)
    sand = set()
    floor = max([p[1] for p in rocks]) + 2

    while (500, 0) not in sand:
      for dx, dy in d:
        next_pos = (sand_pos[0] + dx, sand_pos[1] + dy)
        if next_pos not in rocks and next_pos not in sand and next_pos[1] != floor:
          # sand drop
          sand_pos = next_pos
          break
      else:
        # sand not drop
        sand.add(sand_pos)
        sand_pos = (500, 0)

    return len(sand)

  def parse_data(self, data):
    rock = set()

    for line in data:
      coord = [tuple(map(int, i.split(","))) for i in line.split(" -> ")]
      for i in range(len(coord)-1):
        if coord[i][0] == coord[i+1][0]:
          a, b = sorted([coord[i][1], coord[i+1][1]])
          for y in range(a, b+1):
            rock.add((coord[i][0], y))
        else:
          a, b = sorted([coord[i][0], coord[i+1][0]])
          for x in range(a, b+1):
            rock.add((x, coord[i][1]))

    return rock