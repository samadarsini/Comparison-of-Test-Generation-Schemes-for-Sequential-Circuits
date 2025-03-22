set_messages -log ./test_gen_fl_50.log -replace
read_netlist ./mylib.v
read_netlist ./circuit_sff.v
run_build_model CUT
add_clocks 0 {CK} -shift -timing { 100 50 80 40 }
add_scan_chain chain1 SI SO
add_scan_enables 1 SE
add_pi_constraint 0 SI
add_pi_constraint 0 SE
set_drc -nofile
run_drc
remove_faults -all
set_patterns -delete
set_patterns  -external ./ATPG_pattern_fs_50.pattern
set_faults -model stuck
add_faults -all
run_fault_sim
report_faults -summary
write_faults ./ATPG_pattern_fl_50.left -class UD -class PT -class AU -class ND -replace
exit
