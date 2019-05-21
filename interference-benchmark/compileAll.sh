#!/bin/bash
while read t; do
  echo "Building $t"
  gcc ./benchmarks/$t/*.c -o ./benchmarks/$t/$t
done < tacleNames.txt
