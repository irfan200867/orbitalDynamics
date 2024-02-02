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

fig, axs = plt.subplots(7, 1, sharex=True)

# Remove horizontal space between axes
fig.subplots_adjust(hspace=0)

# Plot each graph
axs[0].set_title(titleClone)
axs[0].plot(df.t, df.a, c='black')
axs[0].annotate(r'$a\;(\mbox{au})$', xy=(1.01*max(df.t), 0.5*(min(df.a) + max(df.a))), \
                xytext=(1.06*max(df.t), 0.5*(min(df.a) + max(df.a))))

axs[1].plot(df.t, df.e, c='red')
axs[1].annotate(r'$e$', xy=(1.01*max(df.t), 0.5*(min(df.e) + max(df.e))), \
                xytext=(1.06*max(df.t), 0.5*(min(df.e) + max(df.e))))

axs[2].plot(df.t, df.Porb, c='blue')
axs[2].annotate(r'$P_{\mbox{\footnotesize orb}}\;(\mbox{yr})$', \
                xy=(1.01*max(df.t), 0.5*(min(df.Porb) + max(df.Porb))), \
                xytext=(1.06*max(df.t), 0.5*(min(df.Porb) + max(df.Porb))))

axs[3].plot(df.t, df.KL, c='green')
axs[3].annotate('KL', xy=(1.01*max(df.t), 0.5*(min(df.KL) + max(df.KL))), \
                xytext=(1.06*max(df.t), 0.5*(min(df.KL) + max(df.KL))))

axs[4].plot(df.t, df.inc, c='magenta')
axs[4].annotate(r'$i\;(^{\circ})$', xy=(1.01*max(df.t), 0.5*(min(df.inc) + max(df.inc))), \
                xytext=(1.06*max(df.t), 0.5*(min(df.inc) + max(df.inc))))

axs[5].set_ylim(0, 400)
axs[5].plot(df.t, df.f, c='orange')
axs[5].annotate(r'$\nu\;(^{\circ})$', xy=(1.01*max(df.t), 0.5*(min(df.f) + max(df.f))), \
                xytext=(1.06*max(df.t), 0.5*(min(df.f) + max(df.f))))

axs[6].set_xlabel(r'$t\;(\mbox{yr})$')
axs[6].set_ylabel(r'$\Omega\;(^{\circ})$', rotation=0)
axs[6].set_ylim(-400, 400)
axs[6].plot(df.t, df.Omg, label=r'$\Omega\;(^{\circ})$')
axs[6].legend(loc='lower left', frameon=False)

axsr = axs[6].twinx()
axsr.set_ylabel(r'$\omega\;(^{\circ})$', rotation=0)
axsr.set_ylim(0, 400)
axsr.plot(df.t, df.omg, 'r--', label=r'$\omega\;(^{\circ})$')
axsr.legend(loc='upper right', frameon=False)

plt.savefig('normalPlotOrbPar'+csvs)
plt.tight_layout()
