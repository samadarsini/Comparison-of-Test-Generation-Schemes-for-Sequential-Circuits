with open("/content/pattern_format.pattern", 'r') as f:
    format = f.read()
random_pattern_50='random_pattern_50.pattern'
with open(random_pattern_50, 'w') as file:
    file.write(format)
with open("/content/test50_1c.txt", 'r') as infile:
    lines = infile.readlines()
    for i, line in enumerate(lines):
        line1 = str(line).rstrip()
        pattern_str = f'"pattern {i}": Call "capture" {{\n"_pi"={line1};\n"_po"=HHHHHHHHXHXXXXLXXXXXXXXXXXXXXXXHXXXXXXXXXXXLHHHHLHHLHHHHHLHLLHHHHLLHHHLHHLHXLHLLLLLLHLHHLHLLLHLLLLHLLHLHLHLHLLXXXXXXLHHXHHHHHHHHHHHXXXXXXXXXXXXXXXXXHH; }}\n'
        with open(random_pattern_50, 'a') as file:
            file.write(pattern_str)
with open(random_pattern_50, 'a') as file:
    file.write('}')