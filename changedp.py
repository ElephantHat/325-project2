#!/usr/bin/python

def getchange(V, A):

    change = [None for x in range(A + 1)]
    change[0] = []
    C=[]
    for j in range(0,len(V)):
        C.append(0)

#generates coins given in change
    for i in range(1, A + 1):
        for v in V:
            if v > i: continue
            elif not change[i] or len(change[i - v]) + 1 < len(change[i]):
                if change[i - v] != None:
                    change[i] = change[i - v][:]
                    change[i].append(v)

#translates change given table to format requested
    for k in change[-1]:
        C[V.index(k)]+=1

#printing results 
    print (C)
    print (len(change[-1]))

    return C, len(change[-1])
