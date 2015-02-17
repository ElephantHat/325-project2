#!/usr/bin/python

import datetime
import fileinput
import json
import changeslow as cs
import changegreedy as cg
import changedp as cdp

inputs = []
V=[]
for line in fileinput.input():
  if (fileinput.lineno() %2 == 1):
    values = line.strip('\[\]\n ').split(',')
    V=[int(i) for i in values]
  else:
    A = int(line)
    inputs.append({'V': V, 'A': A})
  
for test in inputs:
  
  # <--  remove triple quotes around this block to test changeslow. be sure your A values are small... like <25
  
  # Test changeslow
  name = fileinput.filename()[:-4]+ "-change-slow.txt"   #assuming the file input ends with .txt
  f = open(name, "a")
  time1 = datetime.datetime.utcnow()
  coins, change = cs.getchange(test['V'], test['A'])
  finaltime = datetime.datetime.utcnow() - time1
  f.write(json.dumps(coins)+"\n")
  f.write(json.dumps(change)+"\n")
  f.write(json.dumps(finaltime.microseconds)+" microseconds\n")
  f.close()
  

  
  # Test changegreedy
  name = fileinput.filename()[:-4]+ "-change-greedy.txt"   #assuming the file input ends with .txt
  f = open(name, "a")
  time1 = datetime.datetime.utcnow()
  coins, change = cg.getchange(test['V'], test['A'])
  finaltime = datetime.datetime.utcnow() - time1
  f.write(json.dumps(coins)+"\n")
  f.write(json.dumps(change)+"\n")
  f.write(json.dumps(finaltime.microseconds)+" microseconds\n")
  f.close()

  # Test changedp
  name = fileinput.filename()[:-4]+ "-change-dp.txt"   #assuming the file input ends with .txt
  f = open(name, "a")
  time1 = datetime.datetime.utcnow()
  coins, change = cdp.getchange(test['V'], test['A'])
  finaltime = datetime.datetime.utcnow() - time1
  f.write(json.dumps(coins)+"\n")
  f.write(json.dumps(change)+"\n")
  f.write(json.dumps(finaltime.microseconds)+" microseconds\n")
  f.close()
