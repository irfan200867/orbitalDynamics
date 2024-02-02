#!/usr/bin/env python3

import pandas as pd 
import matplotlib.pyplot as plt
from sys import argv


csvf  = argv[1]          # 2020AV2_???_N.csv: ??? = 001 - 243
outf  = argv[2]          # pdf, png, etc...
csvl  = csvf[:-3]+'log'
csvs  = csvf[:-3]+outf

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

fig, axs = plt.subplots(4, 2, sharex=True)             # rows x columns
fig.subplots_adjust(hspace=0)

fig.suptitle(titleClone)

axs[0, 0].plot(df.t, df.a, c='black')     #  row#0, column#0
axs[0, 0].set_ylabel(r'$a\;(\mbox{au})$')#rotation=0)
axs[1, 0].plot(df.t, df.e, c='red')       #  row#1, column#0
axs[1, 0].set_ylabel(r'$e$')#rotation=0)
axs[2, 0].plot(df.t, df.inc, c='magenta') #  row#2, column#0
axs[2, 0].set_ylabel(r'$i\;(^{\circ})$')#rotation=0)
axs[3, 0].plot(df.t, df.KL, c='green')    #  row#3, column#0
axs[3, 0].set_ylabel('KL')#rotation=0)
axs[3, 0].set_xlabel(r'$t\;(\mbox{yr})$')

axs[0, 1].plot(df.t, df.Porb, c='blue')   #  row#0, column#1
axs[0, 1].set_ylabel(r'$P_{\mbox{\footnotesize orb}}\;(\mbox{yr})$')#rotation=0)
axs[0, 1].yaxis.tick_right()

axs[1, 1].set_ylim(0, 400)
axs[1, 1].plot(df.t, df.f, c='orange')    #  row#1, column#1
axs[1, 1].set_ylabel(r'$\nu\;(^{\circ})$')#rotation=0)
axs[1, 1].yaxis.tick_right()

axs[2, 1].set_ylim(-400, 400)
axs[2, 1].plot(df.t, df.Omg)              #  row#2, column#1
axs[2, 1].set_ylabel(r'$\Omega\;(^{\circ})$')#rotation=0)
axs[2, 1].yaxis.tick_right()

axs[3, 1].set_ylim(0, 400)
axs[3, 1].plot(df.t, df.omg, 'r-')       #  row#3, column#1
axs[3, 1].set_ylabel(r'$\omega\;(^{\circ})$')#rotation=0)
axs[3, 1].yaxis.tick_right()
axs[3, 1].set_xlabel(r'$t\;(\mbox{yr})$')

plt.savefig('normalSubplotOrbPar'+csvs)
plt.tight_layout()
