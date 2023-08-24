# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-03 22:34:52
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-11 23:50:04
from utils.solution_base import SolutionBase
import math
import re

ore_list = ["ore", "clay", "obsidian", "geode"]

class Solution(SolutionBase):
  def part1(self, data):
    br_list =  self.parse_data(data)
    # br_elem = (BR_ID, ore robot cost, clay robot cost, obsidian robot ore_cost, obsidian robot clay_cost, geode robot ore_cost, geode robot obsidian_cost)
    # return br_list
    # return self.cal_optimal_geode(br_list[1][1:], 24)
    return sum([br_elem[0]*self.cal_optimal_geode(br_elem[1:], 24) for br_elem in br_list])

  def part2(self, data):
    br_list =  self.parse_data(data)
    return math.prod(self.cal_optimal_geode(br_elem[1:], 32) for br_elem in br_list[:3])

  def parse_data(self, data):
    blueprint = []
    regex = re.compile(r"Blueprint (.*): Each ore robot costs (.*) ore\. Each clay robot costs (.*) ore\. Each obsidian robot costs (.*) ore and (.*) clay\. Each geode robot costs (.*) ore and (.*) obsidian\.")
    for line in data:
      match_result = regex.match(line)
      mr = match_result.groups()
      blueprint.append(tuple(map(int, mr)))
    return blueprint

  def cal_optimal_geode(self, br, minutes: int):
    # BFS search maximum geode
    req = {"ore": {"ore": br[0]},
           "clay": {"ore": br[1]},
           "obsidian": {"ore": br[2], "clay": br[3]},
           "geode": {"ore": br[4], "obsidian": br[5]}}
    max_cost = {t: max(r.get(t, 0) for r in req.values()) for t in req.keys()}
    max_geodes = 0

    resources = {t: 0 for t in ore_list}
    robots = {t: int(t == "ore") for t in ore_list}

    q = []
    q.append((minutes, resources, robots, None))
    while len(q):
      time, resources, robots, last = q.pop()

      # Time end
      if time == 0:
        max_geodes = max(max_geodes, resources["geode"])
        continue

      # Never greater than optimal number
      if max_geodes >= resources["geode"] + time*robots["geode"] + (time-1)*time//2:
        continue
      # print(time, resources, robots)
      time -= 1
      wait = False

      for typ, r in req.items():
        # typ = type
        # r   = robots need resources
        # Enough resource
        if typ != "geode" and resources[typ]+robots[typ]*time > max_cost[typ]*time:
          continue

        # already create
        if (last == None or last == typ) and all(v <= resources[t]-robots[t] for t, v in r.items()):
          continue

        # no resource create robot
        if any(resources[t] < v for t, v in r.items()):
          wait = wait or all(robots[t] > 0 for t in r.keys())
          continue

        next_resources = {t: v+robots[t]-r.get(t,0) for t, v in resources.items()}
        next_robots = {t: v+int(t==typ) for t, v in robots.items()}

        q.append((time, next_resources, next_robots, typ))

      if wait:
        next_resources = {t: v+robots[t] for t, v in resources.items()}
        q.append((time, next_resources, robots, None))

    return max_geodes
