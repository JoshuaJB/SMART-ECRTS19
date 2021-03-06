#!/usr/bin/env bash

# Check that the number of iterations was specified
if [ -z "$1" ]
then
    echo "Usage: $0 <number of iterations>"
    echo "Recommended iterations: between 100 and 1000"
    exit 1
fi

# Setup someplace to store results
mkdir -p results

# Try many epsilons
declare -a epsilons=("01" "055" "1")

for e in "${epsilons[@]}"
do
    # Sets with s (.65,1) and all f
    python3 RunTests.py 4 ${1} results/4_${1}_${e}_65_1_65_1_normal.txt 0 0.65 1 0.65 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_65_1_65_1_normal.txt 0 0.65 1 0.65 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_65_1_65_1_normal.txt 0 0.65 1 0.65 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_65_1_65_1_normal.txt 0 0.65 1 0.65 1 0.${e} &

    python3 RunTests.py 4 ${1} results/4_${1}_${e}_65_1_75_1_normal.txt 0 0.65 1 0.75 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_65_1_75_1_normal.txt 0 0.65 1 0.75 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_65_1_75_1_normal.txt 0 0.65 1 0.75 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_65_1_75_1_normal.txt 0 0.65 1 0.75 1 0.${e} &

    python3 RunTests.py 4 ${1} results/4_${1}_${e}_65_1_85_1_normal.txt 0 0.65 1 0.85 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_65_1_85_1_normal.txt 0 0.65 1 0.85 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_65_1_85_1_normal.txt 0 0.65 1 0.85 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_65_1_85_1_normal.txt 0 0.65 1 0.85 1 0.${e} &

    # Sets with s (.75,1) and all f
    python3 RunTests.py 4 ${1} results/4_${1}_${e}_75_1_65_1_normal.txt 0 0.75 1 0.65 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_75_1_65_1_normal.txt 0 0.75 1 0.65 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_75_1_65_1_normal.txt 0 0.75 1 0.65 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_75_1_65_1_normal.txt 0 0.75 1 0.65 1 0.${e} &

    python3 RunTests.py 4 ${1} results/4_${1}_${e}_75_1_75_1_normal.txt 0 0.75 1 0.75 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_75_1_75_1_normal.txt 0 0.75 1 0.75 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_75_1_75_1_normal.txt 0 0.75 1 0.75 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_75_1_75_1_normal.txt 0 0.75 1 0.75 1 0.${e} &

    python3 RunTests.py 4 ${1} results/4_${1}_${e}_75_1_85_1_normal.txt 0 0.75 1 0.85 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_75_1_85_1_normal.txt 0 0.75 1 0.85 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_75_1_85_1_normal.txt 0 0.75 1 0.85 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_75_1_85_1_normal.txt 0 0.75 1 0.85 1 0.${e} &

    # Sets with s (.85,1) and all f
    python3 RunTests.py 4 ${1} results/4_${1}_${e}_85_1_65_1_normal.txt 0 0.85 1 0.65 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_85_1_65_1_normal.txt 0 0.85 1 0.65 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_85_1_65_1_normal.txt 0 0.85 1 0.65 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_85_1_65_1_normal.txt 0 0.85 1 0.65 1 0.${e} &

    python3 RunTests.py 4 ${1} results/4_${1}_${e}_85_1_75_1_normal.txt 0 0.85 1 0.75 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_85_1_75_1_normal.txt 0 0.85 1 0.75 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_85_1_75_1_normal.txt 0 0.85 1 0.75 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_85_1_75_1_normal.txt 0 0.85 1 0.75 1 0.${e} &

    python3 RunTests.py 4 ${1} results/4_${1}_${e}_85_1_85_1_normal.txt 0 0.85 1 0.85 1 0.${e} &
    python3 RunTests.py 8 ${1} results/8_${1}_${e}_85_1_85_1_normal.txt 0 0.85 1 0.85 1 0.${e} &
    python3 RunTests.py 16 ${1} results/16_${1}_${e}_85_1_85_1_normal.txt 0 0.85 1 0.85 1 0.${e} &
    python3 RunTests.py 32 ${1} results/32_${1}_${e}_85_1_85_1_normal.txt 0 0.85 1 0.85 1 0.${e} &
done
