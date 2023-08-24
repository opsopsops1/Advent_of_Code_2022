# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-26 12:44:32
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-26 15:23:28
from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):
  def part1(self, data):
    return sum([v for v in self.cal_dir_size(data).values() if v <= 100000])

  def part2(self, data):
    dir_size = self.cal_dir_size(data)
    total_used = dir_size["/"]
    need_space = total_used - 40000000
    return min([v for v in dir_size.values() if v >= need_space])

  def cal_dir_size(self, data):
    def calc_sub_dir_size(current_dir):
      dir_total_size[current_dir] = dir_size[current_dir]
      for d in sub_dir[current_dir]:
        dir_total_size[current_dir] += calc_sub_dir_size(d)
      return dir_total_size[current_dir]

    dir_size, sub_dir = self.parse_command_line(data)
    dir_total_size = defaultdict(int)
    dir_total_size["/"] = calc_sub_dir_size("/")
    return dir_total_size

  def parse_command_line(self, data):
    dir_size = {"/": 0}
    sub_dir = defaultdict(list)
    dir_now = []

    idx = 0
    while idx < len(data):
      match data[idx][:4]:
        case "$ cd":
          dir_name = data[idx][5:]
          match dir_name:
            case "..":
              dir_now.pop()
            case _:
              dir_now.append("/" if dir_name == "/" else f"{dir_name}/")
          idx += 1
        case "$ ls":
          idx += 1
          while idx < len(data) and data[idx][0] != '$':
            size, path_name = data[idx].split()
            pwd = "".join(dir_now)
            match size:
              case "dir":
                new_dir = f"{pwd}{path_name}/"
                dir_size[new_dir] = 0
                sub_dir[pwd].append(new_dir)
              case _:
                dir_size[pwd] += int(size)
            idx += 1
    return dir_size, sub_dir
