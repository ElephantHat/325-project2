def changedp(V, A):

    table = [None for x in range(A + 1)]
    table[0] = []
    for i in range(1, A + 1):
        for v in V:
            if v > i: continue
            elif not table[i] or len(table[i - v]) + 1 < len(table[i]):
                if table[i - v] != None:
                    table[i] = table[i - v][:]
                    table[i].append(v)
#This prints the coins used, but not the way the project is supposed to
    if table[-1] != None:
        print (table[-1])
        print (len(table[-1]))

V = [1,2,4]
A = 8

changedp(V, A)
