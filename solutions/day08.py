# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2023-01-26 15:23:43
# @Last Modified by:   Bobo
# @Last Modified time: 2023-01-26 16:46:50
from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    h, w = len(data), len(data[0])
    tallest_U = [-1 for _ in range(w)]
    tallest_D = [-1 for _ in range(w)]
    tallest_L = [-1 for _ in range(h)]
    tallest_R = [-1 for _ in range(h)]
    visible = [[False for i in range(w)] for i in range(h)]
    for h_i in range(1, h-1):
      for w_i in range(1, w-1):
        if int(data[h_i-1][w_i]) > tallest_U[w_i]:
          tallest_U[w_i] = int(data[h_i-1][w_i])
        if tallest_U[w_i] < int(data[h_i][w_i]):
          visible[h_i][w_i] = True
        if int(data[h-h_i][w_i]) > tallest_D[w_i]:
          tallest_D[w_i] = int(data[h-h_i][w_i])
        if tallest_D[w_i] < int(data[h-h_i-1][w_i]):
          visible[h-h_i-1][w_i] = True
    for w_i in range(1, w-1):
      for h_i in range(1, h-1):
        if int(data[h_i][w_i-1]) > tallest_L[h_i]:
          tallest_L[h_i] = int(data[h_i][w_i-1])
        if tallest_L[h_i] < int(data[h_i][w_i]):
          visible[h_i][w_i] = True
        if int(data[h_i][w-w_i]) > tallest_R[h_i]:
          tallest_R[h_i] = int(data[h_i][w-w_i])
        if tallest_R[h_i] < int(data[h_i][w-w_i-1]):
          visible[h_i][w-w_i-1] = True

    return (2*h+2*w-4)+sum(map(sum, visible))

  def part2(self, data):
    h, w = len(data), len(data[0])
    max_score = 0

    for i in range(1, h):
      for j in range(1, w):
        tree_high = int(data[i][j])
        row = data[i]
        col = [x[j] for x in data]
        tree_u = col[:i][::-1]
        tree_d = col[i+1:]
        tree_l = row[:j][::-1]
        tree_r = row[j+1:]

        u_block = [i for i, v in enumerate(tree_u) if int(v) >= tree_high]
        d_block = [i for i, v in enumerate(tree_d) if int(v) >= tree_high]
        l_block = [i for i, v in enumerate(tree_l) if int(v) >= tree_high]
        r_block = [i for i, v in enumerate(tree_r) if int(v) >= tree_high]
        u_score = i if len(u_block) == 0 else u_block[0]+1
        d_score = h-1-i if len(d_block) == 0 else d_block[0]+1
        l_score = j if len(l_block) == 0 else l_block[0]+1
        r_score = w-1-j if len(r_block) == 0 else r_block[0]+1

        max_score = max(max_score, u_score*d_score*l_score*r_score)
    return max_score
