# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-31 22:05:52
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-12 23:18:13
from utils.solution_base import SolutionBase
import re
from collections import defaultdict

class Solution(SolutionBase):
  def part1(self, data):
    def dfs(start, opened_valve, _time):
      pressure = 0
      for valve in opened_valve:
        pressure += flow_rate[valve]
      if _time == 30:
        return pressure
      set_str = str(sorted(opened_valve))
      if set_str in dp[_time][start_idx[start]]:
        return dp[_time][start_idx[start]][set_str]

      moveing_path = 0
      for next_valve in tunnel[start]:
        moveing_path = max(moveing_path, dfs(next_valve, opened_valve, _time+1))
      if start not in opened_valve and flow_rate[start] != 0:
        opened_valve.add(start)
        moveing_path = max(dfs(start, opened_valve, _time+1), moveing_path)
        opened_valve.remove(start)

      dp[_time][start_idx[start]][set_str] = pressure+moveing_path
      return pressure+moveing_path

    flow_rate, tunnel, start_idx = self.get_flow_and_tunnel(data)

    dp = [[dict() for _ in range(len(data)+1)] for ___ in range(31)]
    ans = dfs("AA", set(), 1)
    return ans

  def part2(self, data):
    pass
  
  def get_flow_and_tunnel(self, data):
    flow_rate, tunnel, start_idx = {}, {}, {}

    regex = re.compile(r'Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)')
    for i, line in enumerate(data):
      match_result = regex.match(line)
      src, rate, valve = match_result.group(1), match_result.group(2), match_result.group(3)
      flow_rate[src] = int(rate)
      tunnel[src] = valve.split(", ")
      start_idx[src] = i

    return flow_rate, tunnel, start_idx
