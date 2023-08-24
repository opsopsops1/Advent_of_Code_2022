# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-03 21:31:59
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-03 22:34:30
from utils.solution_base import SolutionBase
from collections import deque

class Solution(SolutionBase):
  def part1(self, data):
    cubes = set([tuple(map(int, line.split(","))) for line in data])
    adjacent_pos = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    sides = 0
    
    for x, y, z in cubes:
      neighbors = [(x+dx, y+dy, z+dz) for dx, dy, dz in adjacent_pos]
      sides += len([1 for nb in neighbors if nb not in cubes])

    return sides

  def part2(self, data):
    cubes = set([tuple(map(int, line.split(","))) for line in data])
    adjacent_pos = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    sides = 0
    
    x_min, x_max = self.minmax([cube[0] for cube in cubes])
    y_min, y_max = self.minmax([cube[1] for cube in cubes])
    z_min, z_max = self.minmax([cube[2] for cube in cubes])
    x_range = range(x_min-1, x_max+2)
    y_range = range(y_min-1, y_max+2)
    z_range = range(z_min-1, z_max+2)

    queue = deque()
    queue.append((x_min-1, y_min-1, z_min-1))
    seen = cubes.copy()

    while queue:
      x, y, z = queue.popleft()
      if (x, y, z) in seen:
        continue

      seen.add((x, y, z))
      neighbors = [(x+dx, y+dy, z+dz) for dx, dy, dz in adjacent_pos]
      sides += len([1 for nb in neighbors if nb in cubes])

      for nb in neighbors:
        if nb not in seen and nb[0] in x_range and nb[1] in y_range and nb[2] in z_range:
          queue.append(nb)

    return sides

  def minmax(self, axis):
    return min(axis), max(axis)
    