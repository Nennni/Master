import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as colors

fname = "Skyserver_SQL2_27_2018 6_51_39 PM.csv"

df2=pd.read_csv(fname)
print(df2)

g=df2[["g"]]
r=df2[["r"]]
g=g.iloc[:,0]  #iloc is the way to produce the plot
r=r.iloc[:,0] 

print(g)
print(r)

gr = g.sub(r)
plt.hist2d(gr,g,bins=100,cmap='magma')
cbar = plt.colorbar()
cbar.set_label('Number of BNSs per cell')
plt.xlim(-0.5,1.5)
plt.show()