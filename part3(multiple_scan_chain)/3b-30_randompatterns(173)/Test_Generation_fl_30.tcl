set_messages -log ./test_gen_fl_30.log -replace
read_netlist ./mylib.v
read_netlist ./circuit_sff.v
run_build_model CUT
add_clocks 0 {CK} -shift -timing { 100 50 80 40 }
add_scan_chain chain1 SI_1 SO_1
add_scan_chain chain2 SI_2  SO_2 
add_scan_chain chain3 SI_3  SO_3 
add_scan_chain chain4 SI_4  SO_4 
add_scan_chain chain5 SI_5  SO_5 
add_scan_chain chain6 SI_6  SO_6 
add_scan_chain chain7 SI_7  SO_7 
add_scan_chain chain8 SI_8  SO_8 
add_scan_chain chain9 SI_9  SO_9 
add_scan_chain chain10 SI_10 SO_10
add_scan_enables 1 SE
add_pi_constraint 0 SE
add_pi_constraint 0 SI_1
add_pi_constraint 0 SI_2
add_pi_constraint 0 SI_3
add_pi_constraint 0 SI_4
add_pi_constraint 0 SI_5
add_pi_constraint 0 SI_6
add_pi_constraint 0 SI_7
add_pi_constraint 0 SI_8
add_pi_constraint 0 SI_9
add_pi_constraint 0 SI_10
run_drc
remove_faults -all
set_patterns -delete
set_patterns  -external ./ATPG_pattern_fs_30.pattern
set_faults -model stuck
add_faults -all
run_fault_sim
report_faults -summary
write_faults ./faults_left_fl_30.left -class UD -class PT -class AU -class ND -replace
exit
