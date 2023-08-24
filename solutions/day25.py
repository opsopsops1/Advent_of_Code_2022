# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-12 17:31:23
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-12 18:33:47
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    return self.d2s(sum([self.s2d(line) for line in data]))

  def part2(self, data):
    pass

  def s2d(self, s):
    convert = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    value = 0
    five = 1
    
    for c in s[::-1]:
      value += five*convert[c]
      five *= 5
    return value

  def d2s(self, d):
    convert = {5: "0", 4: "-", 3: "=", 2: "2", 1: "1", 0: "0"}
    value = d
    number = ""
    carry = 0

    while value:
      r = value%5 + carry
      value = value // 5
      carry = 1 if r > 2 else 0
      number += convert[r]

    if carry:
      number += convert[carry]

    return number[::-1]
