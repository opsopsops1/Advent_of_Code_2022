# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-27 18:35:06
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-27 23:05:13
from utils.solution_base import SolutionBase
from collections import deque
from math import lcm

class Solution(SolutionBase):
  def part1(self, data):
    monkeys = self.take_monkey(data)
    for _ in range(20):
      for monkey_i in monkeys:
        while monkey_i["items"]:
          monkey_i["times"] += 1
          worry = monkey_i["items"].popleft()
          worry = monkey_i["op"](worry) // 3
          test = worry%monkey_i["test"] == 0
          monkeys[monkey_i["target"][test]]["items"].append(worry)
    times = sorted([monkey_i["times"] for monkey_i in monkeys])
    
    return times[-2]*times[-1]

  def part2(self, data):
    monkeys = self.take_monkey(data)
    test_lcm = lcm(*[m["test"] for m in monkeys])
    
    for _ in range(10000):
      for monkey_i in monkeys:
        while monkey_i["items"]:
          monkey_i["times"] += 1
          worry = monkey_i["items"].popleft()
          worry = monkey_i["op"](worry)
          worry %= test_lcm
          test = worry%monkey_i["test"] == 0
          monkeys[monkey_i["target"][test]]["items"].append(worry)
    times = sorted([monkey_i["times"] for monkey_i in monkeys])
    
    return times[-2]*times[-1]
  
  def take_monkey(self, data):
    monkey_data = [monkey.split("\n") for monkey in "\n".join(data).split("\n\n")]
    monkeys = []

    for m_i in monkey_data:
      items = deque(map(int, m_i[1].split(":")[1].strip().split(",")))
      match m_i[2].split(" = ")[1].split():
        case ["old", "*", "old"]:
          op = lambda x: x*x
        case ["old", "*", val]:
          op = lambda x, val=int(val): x*val
        case ["old", "+", val]:
          op = lambda x, val=int(val): x+val
      test = int(m_i[3].split("by ")[1])
      target = [int(m_i[5].split("monkey ")[1]), int(m_i[4].split("monkey ")[1])]
      monkeys.append({"items": items, "op": op, "test": test, "target": target, "times": 0})

    return monkeys