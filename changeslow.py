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
  found = False
  for i, j in enumerate(v):
    if j == c:
      found = True
      break;
  if found:
    #return proper values
    A = []
    for j in range(len(v)):
      if j == i:
        A.append(1)
      else:
        A.append(0)
    return (A, 1)

#TODO: Write the rest of the algorithm...

print getchange([1, 3, 5, 7], 7)
