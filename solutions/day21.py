# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-06 20:53:35
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-06 23:06:43
from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):
  def part1(self, data):
    def find(text):
      val = monkey[text]
      if val.isnumeric():
        return int(val)

      match val[5]:
        case "+":
          return find(val[:4])+find(val[7:])
        case "-":
          return find(val[:4])-find(val[7:])
        case "*":
          return find(val[:4])*find(val[7:])
        case _:
          return find(val[:4])//find(val[7:])

    monkey = defaultdict(str)
    for line in data:
      mon, op = line.split(": ")
      monkey[mon] = op

    return find("root")

  def part2(self, data):
    def find(text):
      val = monkey[text]
      if val.isnumeric():
        return int(val)

      match val[5]:
        case "+":
          return find(val[:4])+find(val[7:])
        case "-":
          return find(val[:4])-find(val[7:])
        case "*":
          return find(val[:4])*find(val[7:])
        case _:
          return find(val[:4])//find(val[7:])


    def has_humn(text):
      if text == "humn":
        include_I.add(text)
        return True
      val = monkey[text]
      if val.isnumeric():
        return False
      
      if has_humn(val[:4]) or has_humn(val[7:]):
        include_I.add(text)
        return True
      return False

    monkey = defaultdict(str)
    for line in data:
      mon, op = line.split(": ")
      monkey[mon] = op
    
    monkey_root = monkey["root"]
    monkey_l, monkey_r = monkey_root[:4], monkey_root[7:]
    include_I = set()

    res1, res2 = has_humn(monkey_l), has_humn(monkey_r)
    if res1:
      monkey_idx = monkey_l
      monkey_val = find(monkey_r)
    else:
      monkey_idx = monkey_r
      monkey_val = find(monkey_l)

    while 1:
      text = monkey[monkey_idx]
      op_l, op_r = text[:4], text[7:]
      if op_l in include_I:
        op_other = find(op_r)
        monkey_idx = op_l
        l_me = True
      else:
        op_other = find(op_l)
        monkey_idx = op_r
        l_me = False

      match text[5]:
        case "+":
          monkey_val -= op_other
        case "-":
          if l_me:
            monkey_val = op_other + monkey_val
          else:
            monkey_val = op_other - monkey_val
        case "*":
          monkey_val = monkey_val // op_other
        case _:
          if l_me:
            monkey_val = op_other * monkey_val
          else:
            monkey_val = op_other // monkey_val
      if monkey_idx == "humn":
        return monkey_val
