# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-28 14:19:22
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-06 01:25:23
from utils.solution_base import SolutionBase
import json
from functools import cmp_to_key

class Solution(SolutionBase):
  def part1(self, data):
    packet = [[*map(json.loads, data[i:i+2])] for i in range(0, len(data), 3)]
    return sum(idx+1 for idx, (a, b) in enumerate(packet) if self.comp(a, b) < 0)
    
  def part2(self, data):
    packet = [*map(json.loads, [i for i in data if i != ""])] + [[[2]], [[6]]]
    packet.sort(key=cmp_to_key(self.comp))
    return (packet.index([[2]])+1)*(packet.index([[6]])+1)
  
  def comp(self, ax, bx):
    a = ax if type(ax) == int else [x for x in ax]
    b = bx if type(bx) == int else [x for x in bx]
    
    idx = 0
    while 1:
      if idx == len(a):
        return -1 if idx < len(b) else None
      if idx >= len(b):
        return 1

      type_a = type(a[idx])
      type_b = type(b[idx])

      if type_a != type_b:
        if type_a == int:
          a[idx] = [a[idx]]
          type_a = type(a[idx])
        else:
          b[idx] = [b[idx]]
          type_b = type(b[idx])
      if type_a == int:
        if a[idx] == b[idx]:
          idx += 1
          continue
        else:
          return -1 if a[idx] < b[idx] else 1
      else:
        res = self.comp(a[idx], b[idx])
        if res in [-1, 1]:
          return res
        else:
          idx += 1
          continue
