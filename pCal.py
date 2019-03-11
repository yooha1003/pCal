#!/usr/bin/env python

# this script is for calculation of p-value from mean and std and subject number

import sys
from scipy.stats import ttest_ind_from_stats

g1_mean = float(sys.argv[1])
g1_std = float(sys.argv[2])
g1_n = float(sys.argv[3])
g2_mean = float(sys.argv[4])
g2_std = float(sys.argv[5])
g2_n = float(sys.argv[6])

pvalue = ttest_ind_from_stats(g1_mean, g1_std, g1_n, g2_mean, g2_std, g2_n)
print pvalue
