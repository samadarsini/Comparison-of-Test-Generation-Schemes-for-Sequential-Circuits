import numpy as np
file_name = "test80_1c.txt"
with open(file_name, "w") as file:
    for i in range(158):
        pattern = ''.join(str(np.random.randint(2)) for j in range(80))
        print(pattern)
        file.write(pattern + '\n')