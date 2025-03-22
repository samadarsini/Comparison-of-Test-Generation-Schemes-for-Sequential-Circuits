import numpy as np
file1 = "/content/fftest30_2b.txt"
with open(file1, 'w') as file:
    for i in range(171):
        pattern = ''.join(str(np.random.randint(2)) for j in range(534))
        file.write(pattern)
        file.write("\n")