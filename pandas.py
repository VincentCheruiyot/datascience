# import pandas as pd
#
# songs={'Album':['Thriller','Man in the mirror','We are the world','Freedom'],
#        'Released':[1980,1990,2000,2010],
#        'Length':['03:50','02:59','04:00','03:56']
# }
# songs_frame=pd.DataFrame(songs)

import numpy as np
a=np.array([0,1,2,3,4])
print(a)

c=np.array([20,1,2,3,5])
c[0]=300
c[4]=250
print(c)

u=[1,2]
v=[3,2]
z=[]

for n,m in zip(u,v):
    z.append(n*m)
    print(z)

import pandas as pd
url:"E:\K&A Tax\Tax\pandas"
df=pd.read_csv(url, header=None)
