# Comparison-of-Test-Generation-Schemes-for-Sequential-Circuits
## Sequential Circuit: Test Pattern Generation and Fault Simulation
This project explores various scan-based test pattern generation schemes and their effectiveness in terms of test coverage, fault coverage, and CPU time. It uses Synopsys TetraMAX for ATPG (Automatic Test Pattern Generation) and fault simulation across multiple scan configurations. The objective is to evaluate how different scan techniques improve testability and efficiency of sequential circuits.

## Features
- Deterministic ATPG Patterns: Generated using Synopsys TetraMAX for precise fault detection.
- Random Pattern Simulation: Simulated at different coverage levels (30%, 50%, 80%) to compare against deterministic ATPG.
- Scan-Based Design Techniques: Evaluation of No Scan, Full Scan, Multi Scan, and Partial Scan configurations.
- Fault Classification: Tracks fault types including Detected, Possibly Detected, Undetectable, ATPG Untestable, and Not Detected.
- TCL-Based Automation: Scripts used to control simulation, pattern application, and coverage extraction.
- Comparative Analysis: Measurement of fault coverage, test coverage, and runtime across all configurations.

## Tools Used
- Synopsys TetraMAX – For ATPG and fault simulation
- Verilog – To describe sequential circuit netlists
- TCL Scripts – For automation of ATPG and simulation processes
- Python – For scan insertion and random test pattern generation
- Google Colab – As development environment

## Summary of Folders
- part1(no_scan) – ATPG patterns and simulation results for original sequential circuit (no scan chain)
- part2(full_scan) – Full scan chain version with maximum testability and coverage
- part3(multiple_scan) – Design using multiple scan chains to reduce test time
- part4(partial_scan) – Design with selected flip-flops scanned for optimized performance
- report – Project report including results, waveforms, tables, and graphs

## Analysis
- No Scan: Provides the lowest test and fault coverage with high CPU runtime, unsuitable for large designs.
- Full Scan: Achieves near 100% coverage with extremely low runtime, ideal for full controllability/observability.
- Multi Scan: Same coverage as full scan with even better test efficiency due to multiple scan paths.
- Partial Scan: Balances coverage and performance when full scan insertion isn't feasible due to area/timing limitations.


