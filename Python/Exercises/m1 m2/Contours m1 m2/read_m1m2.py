import numpy as np

def readm1m2(fname, N):
    #f=file(fname,"r") python2
    f=open(fname,"r")
    (m1,m2) = (
    np.zeros(N,dtype="float"),
    np.zeros(N,dtype="float"))
    i=0
    for linetext in f:
        if(linetext[0]==str("#")):
            continue
        word_list = linetext.split()
        #split splits a line in elements
        if(word_list[0]!=str("#")):
            m1[i]=np.float(word_list[6])
            m2[i]=np.float(word_list[7])
            i=i+1
    #end [ for linetext in f ]
    f.close()
    return (m1,m2)
    
