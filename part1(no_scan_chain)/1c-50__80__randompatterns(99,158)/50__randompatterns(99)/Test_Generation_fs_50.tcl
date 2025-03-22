set_messages -log ./test_gen_fs_50.log -replace
read_netlist mylib.v
read_netlist circuit.v
run_build_model CUT

add_clocks 0 CK
run_drc

remove_faults -all
set_patterns -delete

set_patterns  -external ./random_pattern_50.pattern
set_simulation -measure sim
run_simulation -update
write_patterns ./ATPG_pattern_fs_50.pattern -exclude setup -format stil -external -replace
exit

