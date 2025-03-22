set_messages -log ./test_gen_3a.log -replace
read_netlist ./mylib.v
read_netlist ./circuit_sff.v
run_build_model CUT
add_clocks 0 {CK} -shift -timing { 100 50 80 40 }
add_scan_chains chain1 SI_1 SO_1
add_scan_chains chain2 SI_2 SO_2
add_scan_chains chain3 SI_3 SO_3
add_scan_chains chain4 SI_4 SO_4
add_scan_chains chain5 SI_5 SO_5
add_scan_chains chain6 SI_6 SO_6
add_scan_chains chain7 SI_7 SO_7
add_scan_chains chain8 SI_8 SO_8
add_scan_chains chain9 SI_9 SO_9
add_scan_chains chain10 SI_10 SO_10
add_scan_enables 1 SE
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
add_pi_constraint 0 SE
set_drc -nofile
run_drc
remove_faults -all
set_faults -model stuck
add_faults -all
set_atpg -full_seq_atpg
run_atpg

report_faults -summary
write_patterns  ./ATPG_pattern_3a.pattern -exclude setup -format stil -replace
write_faults faults_list_3a  -uncollapsed -all -replace
write_faults faults_3a_left -class ND -replace
exit

