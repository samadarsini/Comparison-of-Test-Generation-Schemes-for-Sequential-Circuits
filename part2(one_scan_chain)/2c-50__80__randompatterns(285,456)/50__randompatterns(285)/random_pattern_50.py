with open("/content/patternformat.pattern", 'r') as file_in:
    content = file_in.read()
with open('random_pattern_50.pattern', 'a') as file_out:
    file_out.write(content)
with open("/content/test50_2c.txt", 'r') as test, open("/content/fftest50_2c.txt", 'r') as fftest:
    lines_test = test.readlines()
    lines_fftest = fftest.readlines()
    for i in range(len(lines_test)):
        line_test = str(lines_test[i]).rstrip()
        line_fftest = str(lines_fftest[i]).rstrip()
        string1 = (
            f'   "pattern {i + 1}": Call "load_unload" {{\n'
            f'       "SO"=LLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLLHHLL;\n'
            f'       "SI"={line_fftest}; }}\n'
            f'   Call "capture_CK" {{\n'
            f'       "_pi"={line_test};\n'
            f'       "_po"=LHHHHHHHHHHLHLHLLLLHLLHHHHLHLHHHHHHHHLLLHLLLLHHLLLHHLLLHHLLHHLLLLHHHLHLHHHLLHLLHLHLLLLHLLHHLLHLLHHLHLLLHHLHHHHLLHLLHLLHHHLLHHLHHLHLHLHLLHLHLLHHLHHLLHHH; }}\n')
        with open('random_pattern_50.pattern', 'a') as file_out:
            file_out.write(string1)
with open('random_pattern_50.pattern', 'a') as file_out:
    file_out.write('}')