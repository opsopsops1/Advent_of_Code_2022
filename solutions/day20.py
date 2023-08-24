# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-06 16:04:15
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-06 19:21:44
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    x = [(idx, int(i)) for idx, i in enumerate(data)]
    x_len = len(x)

    for i in range(x_len):
      pos, a = [(pos, a) for pos, a in enumerate(x) if a[0] == i][0]
      new_pos = (pos+a[1]+x_len-1)%(x_len-1)

      x.pop(pos)
      x.insert(new_pos, a)

    zero_pos = [i for i, a in enumerate(x) if a[1] == 0][0]
    return x[(zero_pos+1000)%x_len][1] + x[(zero_pos+2000)%x_len][1] + x[(zero_pos+3000)%x_len][1]

  def part2(self, data):
    key = 811589153
    x = [(idx, int(i)*key) for idx, i in enumerate(data)]
    x_len = len(x)
    
    for _ in range(10):
      for i in range(x_len):
        pos, a = [(pos, a) for pos, a in enumerate(x) if a[0] == i][0]
        new_pos = (pos+a[1]+x_len-1)%(x_len-1)

        x.pop(pos)
        x.insert(new_pos, a)

    zero_pos = [i for i, a in enumerate(x) if a[1] == 0][0]
    return x[(zero_pos+1000)%x_len][1] + x[(zero_pos+2000)%x_len][1] + x[(zero_pos+3000)%x_len][1]