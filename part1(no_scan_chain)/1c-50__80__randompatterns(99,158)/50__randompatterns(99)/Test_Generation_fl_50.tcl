set_messages -log ./test_gen_fl_50.log -replace
read_netlist ./mylib.v
read_netlist ./circuit.v
run_build_model CUT

add_clocks 0 CK

run_drc
remove_faults -all
set_patterns -delete
set_patterns  -external ./ATPG_pattern_fs_50.pattern
set_faults -model stuck
add_faults -all
run_fault_sim
report_faults -summary
write_faults ./faults_left_fl_50.left -class UD -class PT -class AU -class ND -replace
exit
