# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-24 22:58:31
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-24 23:54:39
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    pair = 0
    for line in data:
      p = line.split(",")
      p_1 = tuple(map(int, p[0].split("-")))
      p_2 = tuple(map(int, p[1].split("-")))
      if p_1[0] < p_2[0]:
        if p_1[1] >= p_2[1]:
          pair += 1
      elif p_1[0] > p_2[0]:
        if p_1[1] <= p_2[1]:
          pair += 1
      else:
        pair += 1
    return pair
  def part2(self, data):
    pair = 0
    for line in data:
      inv1, inv2 = self.get_section_inteval(line)
      if inv1[0] > inv2[1] or inv2[0] > inv1[1]:
        pair += 1
    return len(data)-pair

  def get_section_inteval(self, section):
    return map(lambda x: tuple(map(int, x.split("-"))), section.split(","))
