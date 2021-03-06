#!/usr/bin/python3

import ModTestParameters
import SMART
import sys
import csv
import os.path

# Required
M = int(sys.argv[1])
TASK_TARGET = int(sys.argv[2])
FILE_OUT = sys.argv[3]

if os.path.isfile(FILE_OUT):
    print("Output file " + FILE_OUT + " already exists. Aborting...")
    exit(1)

# Optional multipliers
ENABLE_OPTIMAL = bool(int(sys.argv[4])) if len(sys.argv) > 5 else False 
STRENGTH_STDEV_MULTIPLIER = int(sys.argv[5]) if len(sys.argv) >= 7 else 1
FRIEND_STDEV_MULTIPLIER = int(sys.argv[6]) if len(sys.argv) >= 7 else 1

# These parameters are derived from a statistical analysis of experimental results
FRIEND_MEAN = STRENGTH_MEAN = 0.715825523745
FRIEND_STDEV = 0.0426836366557
STRENGTH_STDEV = 0.130921998163

# These are fixed parameters chosen subjectively
STEP = .05
utilRanges=[(0, 1), (0, .4), (.3, .7), (.6, 1)] # Wide, low, mid, high. TODO: Bimodel

setsCompleted=1
for utilBound in utilRanges:
    for strength_stdev in [STRENGTH_STDEV * x for x in [STRENGTH_STDEV_MULTIPLIER]]:
        for friend_stdev in [FRIEND_STDEV * x for x in [FRIEND_STDEV_MULTIPLIER]]:
            paramResults = ModTestParameters.runParamTest(ENABLE_OPTIMAL, M, STEP, TASK_TARGET, .5 * M, utilBound[0], utilBound[1], 10, 100, strength_stdev, friend_stdev, STRENGTH_MEAN, FRIEND_MEAN)
            with open(FILE_OUT, "a") as f:
                print("*****", file=f) # Sample delimiter
                csvWriter = csv.writer(f)
                csvWriter.writerow([M, STEP, TASK_TARGET, utilBound[0], utilBound[1], 10, 100, strength_stdev, friend_stdev])
                binSize = M
                for row in paramResults:
                    csvWriter.writerow([binSize] + row)
                    binSize += STEP
            # User-visible status
            print(FILE_OUT, setsCompleted, utilBound[0], utilBound[1], strength_stdev, friend_stdev)
            setsCompleted += 1

print(FILE_OUT, "Complete!")
