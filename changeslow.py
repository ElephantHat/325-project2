#!/usr/bin/python

def getchange(v, c):
  #check if there is a coin of value c
  found = False
  for i, j in enumerate(v):
    if j == c:
      coins = [x*0 for x in range(len(v))]
      coins[i] = 1
      found = True
      return coins, 1
  if not found:
    coins = [x*0 for x in range(len(v))]
    minC = c
    for i in range(c-1, 0, -1):
      coins1, minC1 = getchange(v, i)
      coins2, minC2 = getchange(v, c-i)
      totalC = minC1 + minC2
      if totalC < minC:
        minC = totalC
        coins = [coins1[x] + coins2[x] for x in range(len(v))]
  return coins, minC

print getchange([1, 5, 10, 25, 50], 15)
