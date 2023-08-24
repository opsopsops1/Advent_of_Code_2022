# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-24 19:34:39
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-24 19:56:28
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    score = []
    pair = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    for line in data:
      score += [pair[line]]
    return sum(score)

  def part2(self, data):
    score = []
    pair = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
    for line in data:
      score += [pair[line]]
    return sum(score)
