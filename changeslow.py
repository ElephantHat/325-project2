#!/usr/bin/python
'''
getchange: takes params v and c where:
  v = list of coin values available for making change. Ex: [1, 5, 10, 50]
  c = the value for which we will make change
Returns array A and number min, where:
  A = list of numbers correlating to coins in v. Ex: [0, 0, 1, 2] means zero
      pennies and nickels, 1 dime, and 2 half-dollars
	min = minimum number of coins needed to make change
'''
def getchange(v, c):
  #check if there is a coin of value c
  
  #set flag for base case
  found = False

  #compare each coin value to the amount we are making change for
  for i, j in enumerate(v):
    if j == c:

      #make coin array of all zeroes
      coins = [x*0 for x in range(len(v))]

      #assign proper coin value of 1
      coins[i] = 1

      found = True
      return coins, 1

  #not base case
  if not found:
    #initialize coin value array of all zeroes (probably not needed)
    coins = [x*0 for x in range(len(v))]

    #set minimum number of coins to value we are making change for (it will either be this number, or less)
    minC = c

    # for all values i < K (c) yadda yadda
    for i in range(c-1, 0, -1):
      coins1, minC1 = getchange(v, i)
      coins2, minC2 = getchange(v, c-i)
      totalC = minC1 + minC2
      if totalC < minC:
        minC = totalC
        coins = [coins1[x] + coins2[x] for x in range(len(v))]
  return coins, minC
