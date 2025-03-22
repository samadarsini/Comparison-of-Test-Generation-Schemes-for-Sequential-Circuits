set_messages -log ./test_gen_1a.log -replace
read_netlist ./mylib.v
read_netlist ./circuit.v
run_build_model CUT

add_clocks 0 CK
run_drc

set_faults -model stuck
remove_faults -all

add_faults -all

set_atpg -full_seq_atpg
run_atpg

report_faults -summary
write_patterns  ./ATPG_pattern_1a.pattern -exclude setup -format stil -replace
write_faults faultslist_1a  -uncollapsed -all -replace
write_faults faults_1a_left -class ND -replace
exit

