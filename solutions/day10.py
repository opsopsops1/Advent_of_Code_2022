# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-26 23:54:38
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-27 17:46:15
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    return sum([v*i for i, v in enumerate(self.run_instruction(data)) if i%40 == 20 and i <= 220])

  def part2(self, data):
    x_value = self.run_instruction(data)

    image_char = ["#" if x-1 <= (i-1)%40 <= x+1 else "." for i, x in enumerate(x_value) if i >= 1]
    image = "\n".join("".join(image_char[i:i+40]) for i in range(0, 240, 40))
    return image

  
  def run_instruction(self, instruction):
    x_value = [1]
    now = 1
    for line in instruction:
      if line[:4] == "noop":
        x_value.append(now)
      else:
        for i in range(2):
          x_value.append(now)
        now += int(line.split()[1])
    return x_value
  