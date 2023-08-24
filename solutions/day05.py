# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-25 16:54:25
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-26 11:55:45
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    return "".join([x[-1] for x in self.procedure(data)[1:]])
  def part2(self, data):
    return "".join([x[-1] for x in self.procedure(data, True)[1:]])

  def procedure(self, data, multiple=False):
    sep = [i for i, v in enumerate(data) if v == ""][0]
    
    crates = data[:sep][::-1]
    procedure = data[sep+1:]
    stack_num = int(crates[0].strip()[-1])
    stack = [[] for _ in range(stack_num+1)]

    for line in crates[1:]:
      items = [line[i] for i in range(1, len(line), 4)]
      for i in range(len(items)):
        if items[i] != " ":
          stack[i+1].append(items[i])

    for line in procedure:
      _, c_move, _, c_from, _, c_to = [int(v) if i%2 else v for i, v in enumerate(line.split())]
      move_crates = stack[c_from][-c_move:]
      if multiple is False:
        move_crates = move_crates[::-1]

      stack[c_to].extend(move_crates)
      del stack[c_from][-c_move:]

    return stack
