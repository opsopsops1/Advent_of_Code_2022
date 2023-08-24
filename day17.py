from itertools import cycle
from collections import defaultdict

inp = cycle(enumerate(open(0).read()))
rocks = cycle(  # rows of bits
    enumerate([[120], [32, 112, 32], [112, 16, 16], [64, 64, 64, 64], [96, 96]])
)
M = []  # map
S = []  # sequence of positions of rocks at rest
R = defaultdict(list)  # (rock_idx, instruction_idx) -> S_idx
H = []  # sequence of max heights
L = C = Z = 0  # prefix, cycle length and height per cycle


def fits(rk, x, y):
    return not any(
        M[j] & rk[j - y] >> x for j in range(y, min(len(M), y + len(rk)))
    ) and all(r >> x << x == r for r in rk)


while not C:
    ri, rock = next(rocks)
    x, y = 2, len(M) + 4
    # play rock
    while y and fits(rock, x, y - 1):
        y -= 1
        ai, arrow = next(inp)
        nx = max(0, x - 1) if arrow == "<" else min(7, x + 1)
        x = nx if fits(rock, nx, y) else x

    # update map
    for j, r in enumerate(rock, y):
        if j < len(M):
            M[j] |= r >> x
        else:
            M.append(r >> x)
    H.append(len(M))
    S.append(x)

    # find cycle
    R[(ri, ai)].append(len(S))
    for i, m in enumerate(R[(ri, ai)][:-1]):
        for b in R[(ri, ai)][:i]:
            if m - b == len(S) - m and S[b:m] == S[m:]:
                L, C, Z = m, m - b, len(M) - H[m-1]

height = lambda iters: (Z * ((iters - L) // C) + H[L+((iters - L) % C)-1])
print ("Part1: ", height(2022))
print ("Part1: ", height(1000000000000))

