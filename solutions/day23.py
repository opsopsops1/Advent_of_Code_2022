# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-12 01:37:52
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-12 17:31:40
from utils.solution_base import SolutionBase
from collections import defaultdict

check_point = {"N": [(-1, -1), (-1, 0), (-1, 1)],
               "S": [(1, -1), (1, 0), (1, 1)],
               "W": [(-1, -1), (0, -1), (1, -1)],
               "E": [(-1, 1), (0, 1), (1, 1)],
               "all": [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0)]}

mov = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

class Solution(SolutionBase):
  def part1(self, data):
    elves = self.parse_data(data)
    order = ["N", "S", "W", "E"]
    
    for _ in range(10):
      elf_mov_before = defaultdict(list)
      elves_num = defaultdict(int)
      for (x, y) in elves:
        if all([((x+cx, y+cy) not in elves) for cx, cy in check_point["all"]]):
          # no elve around
          elves_num[(x, y)] += 1
          continue

        elf_new_pos = (x, y)
        for d in order:
          if all((x+cx, y+cy) not in elves for cx, cy in check_point[d]):
            elf_new_pos = (x+mov[d][0], y+mov[d][1])
            break
        
        elves_num[elf_new_pos] += 1
        elf_mov_before[elf_new_pos].append((x, y))

      multi_elves = set(pos for pos, v in elves_num.items() if v > 1)
      new_elves = set(pos for pos, v in elves_num.items() if v == 1)
      
      for pos in multi_elves:
        for bef in elf_mov_before[pos]:
          new_elves.add(bef)

      order = order[1:] + [order[0]]
      elves = new_elves

    # for i in range(12):
    #   for j in range(13):
    #     if (i, j) in elves:
    #       print("#", end='')
    #     else:
    #       print(".", end='')
    #   print()

    x_min, x_max = min(e[0] for e in elves), max(e[0] for e in elves)
    y_min, y_max = min(e[1] for e in elves), max(e[1] for e in elves)
    return (x_max - x_min + 1) * (y_max - y_min + 1) - len(elves)

  def part2(self, data):
    elves = self.parse_data(data)
    order = ["N", "S", "W", "E"]
    
    cnt = 0
    while 1:
      elf_mov_before = defaultdict(list)
      elves_num = defaultdict(int)
      for (x, y) in elves:
        if all([((x+cx, y+cy) not in elves) for cx, cy in check_point["all"]]):
          # no elve around
          elves_num[(x, y)] += 1
          continue

        elf_new_pos = (x, y)
        for d in order:
          if all((x+cx, y+cy) not in elves for cx, cy in check_point[d]):
            elf_new_pos = (x+mov[d][0], y+mov[d][1])
            break
        
        elves_num[elf_new_pos] += 1
        elf_mov_before[elf_new_pos].append((x, y))

      multi_elves = set(pos for pos, v in elves_num.items() if v > 1)
      new_elves = set(pos for pos, v in elves_num.items() if v == 1)
      
      for pos in multi_elves:
        for bef in elf_mov_before[pos]:
          new_elves.add(bef)

      order = order[1:] + [order[0]]
      cnt += 1

      if new_elves == elves:
        return cnt
      elves = new_elves

  def parse_data(self, data):
    return set((x, y) for x, row in enumerate(data) for y, c in enumerate(row) if c == "#")
