# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-31 15:50:06
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-01 21:57:59
from utils.solution_base import SolutionBase
import re

class Line():
  def __init__(self, point, dist, backslash=False):
    self.point = point
    self.dist = dist
    self.y_p = (point[1]-point[0] if not backslash else point[1]+point[0])
    self.backslash = backslash

  def intersection(self, l, space_limit=20):
    if self.backslash == l.backslash:
      if self.y_p == l.y_p:
        if l.point[0] <= self.point[0] <= l.point[0]+l.dist:
          return True, self.point
        if self.point[0] <= l.point[0] <= self.point[0]+self.dist:
          return True, l.point
      return False, ()
    if abs(self.y_p)%2 != abs(l.y_p%2):
      return False, ()
    inter_x = (l.y_p-self.y_p) // 2
    if self.backslash == True:
      inter_x *= -1
    inter_y = inter_x + (self.y_p if self.backslash == False else l.y_p)
    if self.point[0] <= inter_x <= self.point[0] + self.dist and l.point[0] <= inter_x <= l.point[0] + l.dist:
      return True, (inter_x, inter_y)
    return False, ()

class Solution(SolutionBase):
  def part1(self, data):
    range_list, sb_on_row_list = self.find_rowline_range(data, 10 if len(data) == 14 else 2000000)
    range_list.sort()
    return range_list
    range_list_new = [list(range_list[0])] if len(range_list) > 0 else []
    for _range in range_list[1:]:
      for new_range in range_list_new[::]:
        if _range[0] > new_range[1]:
          range_list_new.append(list(_range))
        if new_range[1] >= _range[0] >= new_range[0]:
          new_range[1] = max(new_range[1], _range[1])

    sb_num_on_row = 0
    for beacon in sb_on_row_list:
      for _range in range_list_new:
        if _range[0] <= beacon <= _range[1]:
          sb_num_on_row += 1
          break

    return sum(map(lambda r: r[1]-r[0]+1, range_list_new)) - sb_num_on_row

  def part2(self, data):
    space_limit = (20 if len(data) == 14 else 4000000)
    sensor_list, beacon_list = self.get_sensor_beacon_point(data)
    dist = [abs(sensor_list[i][0]-beacon_list[i][0]) + abs(sensor_list[i][1]-beacon_list[i][1])  for i in range(len(sensor_list))]
    
    line_list = []
    for i in range(len(sensor_list)):
      s = sensor_list[i]
      d = dist[i]
      line_list.append(Line((s[0]-d, s[1]-1), d, backslash=True))
      line_list.append(Line((s[0], s[1]+d+1), d, backslash=True))
      line_list.append(Line((s[0]-d-1, s[1]), d))
      line_list.append(Line((s[0]+1, s[1]-d), d))
    
    inter_list = set()
    for i in range(len(line_list)):
      for j in (range(i+1, len(line_list))):
        is_inter, point = line_list[i].intersection(line_list[j], space_limit)
        if is_inter == True:
          inter_list.add(point)

    inter_list = set([(x, y) for x, y in inter_list if 0 <= x <= space_limit and 0 <= y <= space_limit])
    for inter in inter_list:
      in_shape = False
      for i, s in enumerate(sensor_list):
        if abs(inter[0]-s[0])+abs(inter[1]-s[1]) <= dist[i]:
          in_shape = True
      if not in_shape:
        return inter[0]*4000000 + inter[1]
  
  def find_rowline_range(self, data, row_line):
    sensor_list, beacon_list = self.get_sensor_beacon_point(data)

    range_list = []
    sb_on_row_list = set()
    for i, sensor in enumerate(sensor_list):
      if beacon_list[i][1] == row_line:
        sb_on_row_list.add(beacon_list[i][0])
      if sensor[1] == row_line:
        sb_on_row_list.add(sensor[0])
      d = abs(sensor[0]-beacon_list[i][0]) + abs(sensor[1]-beacon_list[i][1])
      delta = d - abs(sensor[1] - row_line)
      if delta < 0:
        continue
      range_list.append((sensor[0]-delta, sensor[0]+delta))
    return range_list, sb_on_row_list

  def get_sensor_beacon_point(self, data):
    sensor_list = []
    beacon_list = []
    for line in data:
      point_re = re.compile(r"-?\d+")
      sensor, beacon = [tuple(map(int, point_re.findall(x))) for x in line.split(":")]
      sensor_list.append(sensor)
      beacon_list.append(beacon)
    return sensor_list, beacon_list
