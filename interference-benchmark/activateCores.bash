#!/bin/bash
offline_cpus=$(lscpu | grep "Off-line" | cut -d " " -f 4)
echo "Enabling CPU(s): $offline_cpus"
chcpu -e $offline_cpus
