# Define file paths
source_path = "/content/circuit_DFF.v"
target_path = "/content/circuit_sff.v"

# Open and process the input and output files
with open(source_path, "r") as source, open(target_path, "w") as target:
    si_signal = "SI"  # Initialize the scan input signal

    for line in source:
        parts = line.strip().split()  # Tokenize the line
        
        if parts and parts[0] == "DFFX1":
            # Extract the D and Q signals from the line
            d_pin = parts[3][3:-2]  # Extract from ".D(...)" format
            q_pin = parts[4][3:-2]  # Extract from ".Q(...)" format
            
            # Print the instance name for debugging (optional)
            print(f"Processing instance: {parts[1]}")
            
            # Create the transformed line
            updated_line = (
                f"S_DFFX1 S_{parts[1]} {parts[2]} {parts[3]} .SE(SE), .SI({si_signal}), {parts[4]}\n"
            )
            
            # Update the SI signal for the next line
            si_signal = q_pin
            
            # Write the modified line to the target file
            target.write(updated_line)
        else:
            # Write the original line without changes
            target.write(line)
