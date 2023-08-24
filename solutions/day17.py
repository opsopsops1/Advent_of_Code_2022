# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-02-02 19:17:23
# @Last Modified by:   Bobo
# @Last Modified time: 2023-02-12 23:18:51
from utils.solution_base import SolutionBase
from itertools import zip_longest

class Solution(SolutionBase):
  def part1(self, data):
    jets = data[0]
    jet_len = len(jets)
    jet_idx = 0
    above = 3

    rocks = [[
              [0, 0, 1, 1, 1, 1, 0]
             ],
             [
              [0, 0, 0, 1, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0]
             ],
             [
              [0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0]
             ],
             [
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0]
             ],
             [
              [0, 0, 1, 1, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0]
             ]]

    self.room = [[1, 1, 1, 1, 1, 1, 1]]
    rock_idx = 0
    while rock_idx < 2022:
      self.room += [[0, 0, 0, 0, 0, 0, 0] for _ in range(above)]
      this_rock = rocks[rock_idx%5]
      height = len(self.room)
      # print(rock_idx)
      
      while True:
        ori_rock = this_rock
        jet = jets[jet_idx]
        jet_idx = (jet_idx+1)%jet_len

        this_rock = self.rock_push(this_rock, jet)
        if self.check_overlap(this_rock, height):
          this_rock = ori_rock

        height -= 1
        if self.check_overlap(this_rock, height):
          height += 1
          self.rock_stop(this_rock, height)
          rock_idx += 1
          break

    return len(self.room)

  def part2(self, data):
    pass
  
  def rock_push(self, rock, push):
    if push == ">" and sum([i[-1] for i in rock]) == 0:
      rock = [[0]+i[:-1] for i in rock]
    elif push == "<" and sum([i[0] for i in rock]) == 0:
      rock = [i[1:]+[0] for i in rock]
    return rock

  def check_overlap(self, rock, height):
    this_rock = [[0, 0, 0, 0, 0, 0, 0] for _ in range(height)] + rock
    full_height = height + len(rock)

    room = self.room
    if len(room) > full_height:
      room = room[:full_height]
    else:
      room += [[0, 0, 0, 0, 0, 0, 0] for _ in range(full_height-len(room))]

    for h in range(full_height-1, -1, -1):
      roomline = room[h]
      rockline = this_rock[h]
      if sum(rockline) == 0:
        return False
      for x, y in zip(roomline, rockline):
        if x+y > 1:
          return True
    return False

  def rock_stop(self, rock, height):
    room = self.room + [[0, 0, 0, 0, 0, 0, 0]]
    for i in range(len(rock)):
      for j in range(7):
        room[height+i][j] += rock[i][j]
    while sum(room[-1]) == 0:
      room.pop()
    self.room = room
