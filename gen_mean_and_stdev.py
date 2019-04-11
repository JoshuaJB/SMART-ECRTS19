#!/usr/bin/python3
import numpy
import os

if not os.path.isfile("exp_data.csv"):
    print("Please make sure to first follow steps to generate 'exp_data.csv' before running this. Goodbye.")
    exit()

def load_data(filename="exp_data.csv"):
    dat = numpy.loadtxt(open(filename, "rb"), delimiter=",", skiprows=1)

    # Threashold at 1
    super_threshold_indices = dat > 1
    dat[super_threshold_indices] = 1
    return dat

raw_dat = load_data()
rmean, rstd = stats.norm.fit(raw_dat)
print("Mean of 'friendliness': " + str(rmean))
print("Mean of 'resilience': " + str(rstd))

intra_row_stdev = 0
for row in raw_dat:
    row_stdev = numpy.std(row)
    intra_row_stdev += row_stdev / raw_dat.shape[1]

intra_col_stdev = 0
for row in raw_dat.transpose():
    row_stdev = numpy.std(row)
    intra_col_stdev += row_stdev / raw_dat.shape[1]
    
print("Standard deviation of 'friendliness': " + str(intra_row_stdev))
print("Stardard deviation of 'resilience': " + str(intra_col_stdev))


