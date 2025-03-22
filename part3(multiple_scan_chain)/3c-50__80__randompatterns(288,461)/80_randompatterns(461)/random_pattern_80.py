import numpy as np
pattern_format = open("/content/patternformat.pattern").read()
input_file = "/content/test80_3c.txt"
output_file = 'random_pattern_80.pattern'
with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
    lines = infile.readlines()
    for i, line in enumerate(lines):
        lst = line.split(" ")
        strin = f'\n   "pattern {i + 1}": Call "load_unload" {{\n'
        strin1 = ''
        for so in range(1, 5):
            strin1 += f'     "SO_{so}"=LLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLL;\n'
        strin2 = ''
        for so in range(5, 11):
            strin2 += f'     "SO_{so}"=HLHLHHLLHLLHLHLLLLHLLLLHLLLLLLLHHHLLLLHHLHLHLLLLLLLLL;\n'
        string = strin + strin1 + strin2
        str_si = ''
        for si in range(1, 11):
            str_si += f'     "SI_{si}"={lst[si]};\n'
        str_po = '} \n   Call "capture_CK" {\n'
        str_po += f'     "_pi"={lst[0]};\n'
        str_po += '     "_po"=HLLLHHLHLHHHHHHHHHHHHHLHLHLHHLHLLHHHHHHLLLLLLLHLLLHLLLLLLLHHLHLLLLHHHHLHHLLLLLLHLHHLLLHLLLLLHLHHLHHHLHHLLHHLLHHHHHHHHLLLHHHLHLHHHLHHHHHHHHHHHHHHLHLLHHHLHLHLHHLL; }\n'
        string1 = pattern_format + string + str_si + str_po
        outfile.write(string1)
    outfile.write('}')