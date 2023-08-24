# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-26 11:56:24
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-26 12:25:28
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    return self.find_marker(data[0], 4)

  def part2(self, data):
    return self.find_marker(data[0], 14)
  
  def find_marker(self, data, size):
    for i in range(len(data)-size+1):
      ds = set(data[i:i+size])
      if len(ds) == size:
        return i+size
  