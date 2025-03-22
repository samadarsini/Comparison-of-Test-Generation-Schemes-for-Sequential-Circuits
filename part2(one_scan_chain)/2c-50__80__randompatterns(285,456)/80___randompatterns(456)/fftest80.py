import numpy as np
file1 = "/content/fftest80_2c.txt"
with open(file1, 'w') as file:
    for i in range(456):
        pattern = ''.join(str(np.random.randint(2)) for j in range(534))
        file.write(pattern)
        file.write("\n")