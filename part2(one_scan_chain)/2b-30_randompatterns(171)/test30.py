import numpy as np
file1 = "/content/test30_2b.txt"
with open(file1, 'w') as file:
    for i in range(171):
        pattern = ''.join(str(np.random.randint(2)) for j in range(82))
        file.write(pattern)
        file.write("\n")