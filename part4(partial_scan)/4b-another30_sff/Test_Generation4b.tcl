set_messages -log ./test_gen_4b.log -replace
read_netlist ./mylib.v
read_netlist ./circuit_ran30sff.v
run_build_model CUT
add_clocks 0 {CK} -shift -timing { 100 50 80 40 }
add_scan_chain chain1 SI SO
add_scan_enables 1 SE
add_pi_constraint 0 SI
add_pi_constraint 0 SE
set_drc -nofile
run_drc
remove_faults -all
set_faults -model stuck
add_faults -all
set_atpg -full_seq_atpg
run_atpg

report_faults -summary
write_patterns  ./ATPG_pattern_4b.pattern -exclude setup -format stil -replace
write_faults faults_list_4b  -uncollapsed -all -replace
write_faults faults_4b_left -class ND -replace
exit

