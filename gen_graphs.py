#!/usr/bin/python3

# Switch to a backend that doesn't need X
import matplotlib
matplotlib.use("Agg")

# Switch to a font with Unicode characters
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', 'sans-serif']
rcParams['font.serif'] = ['DejaVu Serif', 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook', 'Century Schoolbook L', 'Utopia', 'ITC Bookman', 'Bookman', 'Nimbus Roman No9 L', 'Times New Roman', 'Times', 'Palatino', 'Charter', 'serif']

import sys
import os
import matplotlib.pyplot as plt
import numpy

def read_sample(file):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        line = file.readline()
        if line == b"*****\n":
            break
        if not line or line == "":
            break
        #    raise Exception("No more data to read from this sample file.")
        yield line

def load_data(file):
    header = file.readline()
    if not header:
        return (None,None)
    return (numpy.loadtxt(read_sample(file), delimiter=",", usecols=(0,1,2,3,4,5,6)), header.decode("utf-8").strip())

def util_header(header):
    elems = header.split(',')
    range_str = ""
    if float(elems[3]) == 0:
        range_str += "({0:.1f}, "
    else:
        range_str += "[{0:.1f}, "    
    if float(elems[4]) == 1:
        range_str += "{1:.1f})"
    else:
        range_str += "{1:.1f}]"
    return "Task Utilization ∈ " + range_str.format(float(elems[3]),float(elems[4]))

def format_header(header, util_on=True):
    elems = header.split(',')
    # Autodetect if this is uniform by inspecting the field count
    if len(elems) > 10:
        cores = "{0} Cores, ".format(int(elems[0]))
        utile = util_header(header) + ", ϵ = {0:.3f}\n" if util_on else "ϵ = {0:.3f}, "
        utile = utile.format(float(elems[11]))
        sf = "s ∈ Uniform({0:.2f},{1:.2f}), f ∈ Uniform({2:.2f},{3:.2f})".format(float(elems[7]), float(elems[8]), float(elems[9]), float(elems[10]))
        return cores + utile + sf
    else:
        cores = "{0} Cores, ".format(int(elems[0]))
        util = util_header(header) + "\n" if util_on else ""
        sf = "s ∈ Gauss(0.72,{0:.2f}), f ∈ Gauss(0.72,{1:.2f})".format(float(elems[7]), float(elems[8]))
        return cores + util + sf

def setup_figure(fig, header):
    fig.legend(["Oʙʟɪᴠɪᴏᴜs", "Gʀᴇᴇᴅʏ-Tʜʀᴇᴀᴅ", "Gʀᴇᴇᴅʏ-Pʜʏsɪᴄᴀʟ", "Gʀᴇᴇᴅʏ-Mɪxᴇᴅ", "Oᴘᴛɪᴍᴀʟ"])
    fig.set_ylim(0,1.02)
    fig.set_xlabel('Utilization')
    fig.set_ylabel('Schedulability Ratio')
    fig.set_title(header)

def add_plot(target, dat, m_range_multiplier=2):
    # Divide, but ignore if divisor is 0
    UMA_cols = dat[:,2:6].T
    task_count = dat[:,1]
    util_bins = dat[:,0]
    things = numpy.divide(UMA_cols, task_count, out=numpy.zeros_like(UMA_cols), where=task_count!=0).T
    # Crop charts
    stop_idx = len(util_bins) - 1
    for idx in range(len(util_bins)):
        if util_bins[idx] > util_bins[0] * m_range_multiplier:
            stop_idx = idx
            break
    # Plot
    target.plot(util_bins[:stop_idx], things[:stop_idx])
    
def plot_util_quad_from_file(path, m_range_multiplier=2, save=False):
    file = open(path, "rb")
    file.readline() # Dump first line
    fig = plt.figure()
    cached_header = ""
    for i in range(1,5):
        dat, header = load_data(file)
        if dat is None:
            break
        cached_header = header
        etc = fig.add_subplot(2,2,i)
        add_plot(etc, dat, m_range_multiplier)
        setup_figure(etc, util_header(header))
    fig.suptitle(format_header(cached_header, util_on=False), fontsize=18)
    fig.tight_layout(rect=[0, 0.03, 1, 0.90])
    if not save:
        plt.show()
    else:
        plt.savefig(sdir + format_header(cached_header, util_on=False) + ".pdf")
    plt.close(fig)

plt.rcParams['figure.figsize'] = [12, 9]
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <sample count in set to plot>")
    exit()
else:
    sample_size_to_scan = int(sys.argv[1])

# Plot Gaussion-Average Data
wdir = "gaussian-average/results/"
sdir = "gaussian-average/results/graphs/"
if not os.path.exists(sdir):
    os.mkdir(sdir)
print("Scanning all gaussian-average "+str(sample_size_to_scan)+"-sample results and saving to '" + sdir + "'...")
for core in ["4","8","16","32"]:
    for f in range(1,4):
        for s in range(1,4):
            plot_util_quad_from_file(wdir+core+"_"+str(sample_size_to_scan)+"_"+str(f)+"_"+str(s)+"_normal.txt", save=True)
print("Done.")

# Plot Uniform-Normal Data
wdir = "uniform-normal/results/"
sdir = "uniform-normal/results/graphs/"
if not os.path.exists(sdir):
    os.mkdir(sdir)
print("Scanning all uniform-normal "+str(sample_size_to_scan)+"-sample results and saving to '" + sdir + "'...")
r = ["65","75","85"]
for core in ["4","8","16","32"]:
    for f in r:
        for s in r:
            for e in ["01","055","1"]:
                plot_util_quad_from_file(wdir+core+"_"+str(sample_size_to_scan)+"_"+str(e)+"_"+str(f)+"_1_"+str(s)+"_1_normal.txt", save=True)
print("Done.")

