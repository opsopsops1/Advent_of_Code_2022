# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-24 22:08:18
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-26 01:49:38
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    def get_only_item(compartments):
      alpha_l = {}
      alpha_r = {}
      compartments_len = len(compartments)
      compartments_l = compartments[:compartments_len//2]
      compartments_r = compartments[compartments_len//2:]
      for i in range(compartments_len//2):
        alpha_l[compartments_l[i]] = alpha_l.get(compartments_l[i], 0) + 1
        alpha_r[compartments_r[i]] = alpha_r.get(compartments_r[i], 0) + 1
      for k in alpha_l.keys():
        if k not in alpha_r:
          continue
        return k

    def get_item_priority(item):
      return (ord(item)-96 if item.islower() else ord(item)-38)

    priority = []
    for line in data:
      priority += [get_only_item(line)]
    # print(priority)
    return sum(list(map(get_item_priority, priority)))

  def part2(self, data):
    priority = []
    for i in range(0, len(data), 3):
      rucksack1, rucksack2, rucksack3 = map(set, data[i:i+3])
      item = rucksack1.intersection(rucksack2, rucksack3).pop()
      priority += [ord(item) - (96 if item.islower() else 38)]
    return sum(priority)
