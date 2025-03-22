f= open ("/content/test80_2c.txt",'w')
import numpy as np
for i in range (0,456):

    patt=''
    for bits in range (0,82):
        patt0= np.random.randint(2, size=1)
        ps= str(patt0).replace(" ", "")[1:-1]
        patt=patt+ps
        
    print(patt)
    f.write(patt)
    f.write('\n')
    

f.close()

