# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-23 22:43:05
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-23 23:12:32
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    items = self.parse_items(data)
    return max(items)
  def part2(self, data):
    items = self.parse_items(data)
    return sum(sorted(items)[-3:])
  def parse_items(self, data):
    return [sum(map(int, elf.split("\n"))) for elf in "\n".join(data).split("\n\n")]
