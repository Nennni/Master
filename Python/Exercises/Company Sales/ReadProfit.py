
#contains the user-provided function to read a file in a fast way
import numpy as np



def readfast(fname, N):
    #f=file(fname,"r") python2
    f=open(fname,"r")
    (month,facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer) = (
        np.zeros(N,dtype="int"),
        np.zeros(N,dtype="int"),
        np.zeros(N,dtype="int"),
        np.zeros(N,dtype="int"),
        np.zeros(N,dtype="int"),
        np.zeros(N,dtype="int"),
        np.zeros(N,dtype="int"))
    i=0
    for linetext in f:
        if(linetext[0]==str("#")):
            continue
        word_list = linetext.split()
        #split splits a line in elements
        if(word_list[0]!=str("#")):
            month[i]=np.int(word_list[0])
            facecream[i]=np.int(word_list[1])
            facewash[i]=np.int(word_list[2])
            toothpaste[i]=np.int(word_list[3])
            bathingsoap[i]=np.int(word_list[4])
            shampoo[i]=np.int(word_list[5])
            moisturizer[i]=np.int(word_list[6])
            i=i+1
    #end [ for linetext in f ]
    f.close()
    return (month,facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer)


#fname="output.txt" #output filename as a string
#f=open(fname,"w")  #I create file with filename
                   #the new file will be for writing (w)
#f.write("# Time(Myr), Mass(Msun), He(Msun), CO(Msun) \n")
#for i in range(len(evoltime)):
 #   if(mass[i]!=0.0):
  #      f.write(str(evoltime[i])+" "+str(mass[i])+" "+ \
   #             str(massHe[i])+" "+str(massCO[i])+"\n")

