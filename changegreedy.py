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
  A=[]
  min=0

  for i in range(len(v)):
    A.append(0)

  i=len(v)-1

  while c>0:
    if v[i] <= c:
      c -= v[i]
      min += 1
      A[i] += 1
    else:
      i -= 1


  return (A, min)
