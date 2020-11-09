
#contains the user-provided function to read a file in a fast way
import numpy as np



def readchirpmass(fname, N):
    #f=file(fname,"r") python2
    f=open(fname,"r")
    chirpm = (np.zeros(N,dtype="float"))
    i=0
    for linetext in f:
        if(linetext[0]==str("#")):
            continue
        word_list = linetext.split()
        #split splits a line in elements
        if(word_list[0]!=str("#")):
            chirpm[i]=np.float(word_list[0])
            i=i+1
    #end [ for linetext in f ]
    f.close()
    return (chirpm)

def readtmerg(fname, N):
    #f=file(fname,"r") python2
    f=open(fname,"r")
    tmerg = (
        np.zeros(N,dtype="float"))
    i=0
    for linetext in f:
        if(linetext[0]==str("#")):
            continue
        word_list = linetext.split()
        #split splits a line in elements
        if(word_list[0]!=str("#")):
            tmerg[i]=np.float(word_list[0])
            i=i+1
    #end [ for linetext in f ]
    f.close()
    return (tmerg)



#fname="output.txt" #output filename as a string
#f=open(fname,"w")  #I create file with filename
                   #the new file will be for writing (w)
#f.write("# Time(Myr), Mass(Msun), He(Msun), CO(Msun) \n")
#for i in range(len(evoltime)):
 #   if(mass[i]!=0.0):
  #      f.write(str(evoltime[i])+" "+str(mass[i])+" "+ \
   #             str(massHe[i])+" "+str(massCO[i])+"\n")

