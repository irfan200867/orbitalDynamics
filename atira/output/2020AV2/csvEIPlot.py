#!/usr/bin/env python3

import pandas as pd 
import matplotlib.pyplot as plt
from sys import argv


#headers = ['t', 'dt', 'x', 'y', 'z', 'dcSun', 'dsSun', 'Rsun', 'dcMer', 'dsMer', 'tRhMer', 'Rmer', 'dcVen', 'dsVen', 'tRhVen', 'Rven', 'dcEar', 'dsEar', 'tRhEar', 'Rear', 'dcMar', 'dsMar', 'tRhMar', 'Rmar', 'dcJup', 'dsJup', 'tRhJup', 'Rjup', 'dcSat', 'dsSat', 'tRhSat', 'Rsat', 'dcUra', 'dsUra', 'tRhUra', 'Rura', 'dcNep', 'dsNep', 'tRhNep', 'Rnep', 'a', 'perihel', 'e', 'Porb', 'KL', 'inc', 'Omg', 'omg', 'f', 'E', 'J', 'enc', 'pln']

csvf  = argv[1]          # 2020AV2_???_N.csv: ??? = 001 - 243
csvl  = csvf[:-3]+'log'
csvs  = csvf[:-3]+'pdf'

df    = pd.read_csv(csvf)
logf  = open(csvl, 'r')
lines = logf.readlines()

count = 0
# Strips the newline character
for line in lines:
    count += 1
    if count == 7:
       sep = ' W'
       line[22:].strip()
       aste  = line[22:].strip().split(sep, 1)[0]
    if count == 10:
       sep = ')'
       line[22:].strip()
       combi = line[22:].strip().split(sep, 1)[0]+sep
    if count == 15:
       clone = line[26:29].strip()

logf.close()

titleClone = r'Cloning \#'+clone+' of \\textbf{'+aste+'} : $'+combi+'\\times('\
             +'\sigma_a, \sigma_e, \sigma_i, \sigma_{\Omega}, \sigma_{\omega})$'

plt.rcParams.update({
    "text.usetex": True,
    "ps.usedistiller": "xpdf",
})

plt.title(titleClone)
plt.xlabel(r'$e$')
plt.ylabel(r'$i\;(^{\circ})$', rotation=0)
plt.xlim(0, 0.30)
#plt.xlim(0, 1.10*max(df.e))
plt.ylim(0, 1.10*max(df.inc))

# 1st datapoint
plt.scatter(df.e[0], df.inc[0], s=5, c='red', label=r'$\mathbf{F} \equiv (e_0,\,i_0)$')
# 1st 25%  datapoints
plt.scatter(df.e[1:len(df.e)//4], df.inc[1:len(df.inc)//4], s=5, c='blue', label=r'$1^{\mbox{\footnotesize st}}$ 25\% data')
# 2nd 25%  datapoints
plt.scatter(df.e[len(df.e)//4:len(df.e)//2], df.inc[len(df.inc)//4:len(df.inc)//2], s=5, c='green', label=r'$2^{\mbox{\footnotesize nd}}$ 25\% data')
# 3rd 25%  datapoints
plt.scatter(df.e[len(df.e)//2:3*len(df.e)//4], df.inc[len(df.inc)//2:3*len(df.inc)//4], s=5, c='magenta', label=r'$3^{\mbox{\footnotesize rd}}$ 25\% data')
# 4th 25%  datapoints
plt.scatter(df.e[3*len(df.e)//4:-1], df.inc[3*len(df.inc)//4:-1], s=5, c='orange', label=r'$4^{\mbox{\footnotesize th}}$ 25\% data')
# last datapoint
plt.scatter(df.e[len(df.e) - 1], df.inc[len(df.inc) - 1], s=5, c='black', label=r'$\mathbf{L} \equiv (e_{\mbox{\footnotesize last}},\,i_{\mbox{\footnotesize last}})$')

# other datapoints
# plt.scatter(df.e[1:len(df.e) - 1], df.inc[1:len(df.inc) - 1], s=5, label=r'other values')

plt.legend(loc='best', frameon=False)

plt.annotate(r'$\mathbf{F}$', xy=(df.e[0], df.inc[0]), xytext=(df.e[0], 1.02*df.inc[0]))
plt.annotate(r'$\mathbf{L}$', xy=(df.e[len(df.e) - 1], df.inc[len(df.inc) - 1]), xytext=(df.e[len(df.e) - 1], 1.03*df.inc[len(df.inc) - 1]))

plt.savefig('normalPlotEccVsInc'+csvs)
plt.tight_layout()
