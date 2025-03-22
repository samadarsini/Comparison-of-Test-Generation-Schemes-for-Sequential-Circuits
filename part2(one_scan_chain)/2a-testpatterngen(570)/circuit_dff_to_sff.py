output_file = "/content/circuit_sff.v"
input_file = "/content/circuit_DFF.v"

with open(output_file, "w") as circuit_sff, open(input_file, 'r') as f:
    lines = f.readlines()
    si = "SI"
    for line in lines:
        line1 = line.split()
        if line1 and line1[0] == "DFFX1":
            d = str(line1[3]).strip(".D(").strip("),")
            q = str(line1[4]).strip(".Q(").strip("));")
            print(line1[1])
            a = f"S_DFFX1 S_{line1[1]} {line1[2]} {line1[3]} .SE(SE), .SI({si}), {line1[4]}\n"
            si = q
            circuit_sff.write(a)
        else:
            circuit_sff.write(line)

