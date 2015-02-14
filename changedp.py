import fileinput

def changedp(V, A, name):

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

#Writing to file.....does it really need to be this complicated?
    fileOut=open(name,"a")
    fileOut.write("[")
    for i in range(0,len(C)):
        fileOut.write(str(C[i]))
        if i!=len(C)-1:
            fileOut.writelines(",")
    fileOut.write("]\n")
    fileOut.write(str(len(change[-1])))
    fileOut.write("\n")
    fileOut.close()




V=[]
for line in fileinput.input():
    if (fileinput.lineno() %2 == 1):
        V[:]=[]
        V=line[1:-3]
        V=V.split(',')
        V=[int(i) for i in V]
    else:
        A = int(line)
        name = fileinput.filename()[:-4]+ "change.txt"   #assuming the file input ends with .txt
        changedp(V, A, name)

