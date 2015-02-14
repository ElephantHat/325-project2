#!/usr/bin/python

import changegreedy as greedy

v=[1,5, 10, 25]
c = 240
minC = c


for k in range(c, 0, -1):
  coinarray1, coins1 = greedy.getchange(v, k)
  coinarray2, coins2 = greedy.getchange(v, c-k)

  if (coins1+coins2) < minC:
    minC = coins1 + coins2
    minK = k
    numC = [coinarray1[x] + coinarray2[x] for x in range(len(v))]

return (numC, minC)
