import numpy as np
file_name = "test30_1b.txt"
with open(file_name, "w") as file:
    for i in range(60):
        pattern = ''.join(str(np.random.randint(2)) for j in range(80))
        print(pattern)
        file.write(pattern + '\n')