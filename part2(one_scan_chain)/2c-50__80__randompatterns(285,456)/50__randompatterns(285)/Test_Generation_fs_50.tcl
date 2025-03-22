set_messages -log ./test_gen_fs_50.log -replace
read_netlist ./mylib.v
read_netlist ./circuit_sff.v
run_build_model CUT

add_clocks 0 {CK} -shift -timing { 100 50 80 40 }
add_scan_chain chain1 SI SO
add_scan_enables 1 SE
add_pi_constraint 0 SE
add_pi_constraint 0 SI

run_drc

remove_faults -all
set_patterns -delete

set_patterns -external ./random_pattern_50.pattern

set_simulation -measure sim
run_simulation -update
write_patterns ./ATPG_pattern_fs_50.pattern -exclude setup -format stil -external -replace
#write_faults faults_list_1  -uncollapsed -all -replace
#write_faults faults_left -class ND -replace
exit

