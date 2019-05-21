#!/bin/bash
core_count=$(grep -c ^processor /proc/cpuinfo)
for ((i=core_count/2;i<core_count;i++))
do
    chcpu -d $i
done
