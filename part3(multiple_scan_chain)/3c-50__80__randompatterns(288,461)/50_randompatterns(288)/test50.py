import numpy as np
file1 = "test50_3c.txt"
with open(file1, "w") as file:
    for p in range(288):
        pattern = ''
        for so in range(11):
            if so == 0:
                bits = 91
            elif 1 <= so < 5:
                bits = 54
            elif 5 <= so <= 10:
                bits = 53
            pattern1 = ''.join(str(np.random.randint(2)) for j in range(bits))
            pattern += pattern1 + " "
        print(pattern)
        file.write(pattern.strip())
        file.write("\n")