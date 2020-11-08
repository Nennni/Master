import numpy as np

def read(fname,N):
    #f=file(fname,"r") python2
    f=open(fname,"r")
    (metallicity,m1,m2,t) = (
    np.zeros(N,dtype="float"),
    np.zeros(N,dtype="float"),
    np.zeros(N,dtype="float"),
    np.zeros(N,dtype="float"))
    i=0
    for linetext in f:
        if(linetext[0]==str("#")):
            continue
        word_list = linetext.split()
        #split splits a line in elements
        if(word_list[0]!=str("#")):
            metallicity[i]=np.float(word_list[3])
            m1[i]=np.float(word_list[6])
            m2[i]=np.float(word_list[7])
            t[i]=np.float(word_list[8])
            i=i+1
    #end [ for linetext in f ]
    f.close()
    return (metallicity,m1,m2,t)
