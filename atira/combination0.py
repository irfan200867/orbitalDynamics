#!/usr/bin/env python3
# coding: utf-8

import rebound
import numpy as np
from asteroids import *
from datetime import datetime
from sys import argv


def titlef(logfile):
    logfile.write('***************************************************************\n')
    logfile.write('* REBOUND simulation of asteroid (w/o Post-Newtonian effects) *\n')
    logfile.write('*                                                             *\n')
    logfile.write('* (c) P2MI 2023 project: MIH & ES                             *\n')
    logfile.write('***************************************************************\n')
    return


idx   = int(argv[1])   # 19, 25 int
Tint  = float(argv[2]) # float
Nout  = int(argv[3])   # int


clsaas = [0, 1, -1]
clsecc = [0, 1, -1]
clsinc = [0, 1, -1]
clsOMG = [0, 1, -1]
clsomg = [0, 1, -1]
 
combi = []
 
for i in range(len(clsaas)):
    for j in range(len(clsecc)):
        for k in range(len(clsinc)):
            for l in range(len(clsOMG)):
                for m in range(len(clsomg)):
                    combi.append((clsaas[i], clsecc[j], clsinc[k], clsOMG[l], clsomg[m]))


out0   = list(atira.items())[idx][0]
out    = list(atira.items())[idx][1]


#for i in range(2):
for i in range(len(combi)):
    outdat = open(out+'_'+f'{i+1:03d}'+'_N.csv', 'w')
    outlog = open(out+'_'+f'{i+1:03d}'+'_N.log', 'w')
    
    titlef(outlog)
    
    outlog.write(f'\n*** LOG SIMULATION OF {out0} WITH {Nout} POINTS, AND {Tint} YR INTEGRATION TIME ***\n')

    sim = rebound.Simulation()
    sim.units = ('msun', 'au', 'yr2pi')
    
    for j in range(len(major_bodies)):
        sim.add(list(major_bodies.items())[j][0])
    
    sim.add(list(atira.items())[idx][0])
    
    sim.move_to_com()
    ps = sim.particles
    
    aori = ps[9].a
    eori = ps[9].e
    iori = ps[9].inc
    Oori = ps[9].Omega
    oori = ps[9].omega
    
    aasi = ps[9].a     + combi[i][0] * list(atira_Sa.items())[idx][1]
    ecci = ps[9].e     + combi[i][1] * list(atira_Se.items())[idx][1]
    inci = ps[9].inc   + combi[i][2] * list(atira_Si.items())[idx][1] * np.pi / 180
    OMGi = ps[9].Omega + combi[i][3] * list(atira_SO.items())[idx][1] * np.pi / 180
    omgi = ps[9].omega + combi[i][4] * list(atira_So.items())[idx][1] * np.pi / 180
    
    sim = None
    
    outlog.write(f'*** RESTART FOR ADOPTING SOME CLONING VALUES OF {list(atira.items())[idx][0]} ***\n')

    sim = rebound.Simulation()
    sim.units = ('msun', 'au', 'yr2pi')
    
    for k in range(len(major_bodies)):
        sim.add(list(major_bodies.items())[k][0])
    sim.add(m=0, a=aasi, e=ecci, inc=inci, Omega=OMGi, omega=omgi)
    sim.move_to_com()
    ps = sim.particles
    N  = len(ps)

    
    outlog.write(f'*** Adding particle #{len(ps)} as clone #{i+1:03d}/{len(combi):03d} of {list(atira.items())[idx][0]} ***\n')
    outlog.write(f"*** Using combination {combi[i]} for its 5-sigma's***\n")
    outlog.write(f'*** Original values of a [au], e, inc [rad], Omega [rad], and omega [rad] '\
                 f'as of {datetime.now()} are:\n')
    outlog.write(f'a = {aori:11.9E}, e = {eori:11.9E}, i = {iori:11.9E}, '\
                 f'Omega = {Oori:11.9E}, and omega = {oori:11.9E}\n')
    outlog.write(f'*** Cloning values become:\n')
    outlog.write(f'a = {aasi:11.9E}, e = {ecci:11.9E}, i = {inci:11.9E}, '\
                 f'Omega = {OMGi:11.9E}, and omega = {omgi:11.9E}\n')
    outlog.write(f'*** CONTINUING SIMULATION {i+1:03d}/{len(combi):03d}, combination {combi[i]}, starting from {datetime.now()}...\n')

    outlog.write(f'Columns name in output file: {out}_{i+1:03d}_N.csv\n')
    outlog.write(' 1. t [yr]\n 2. dt [yr]\n'\
             ' 3. x [au]\n 4. y [au]\n 5. z [au]\n'\
             ' 6. dcSun [au] (to center of Sun)\n 7. dsSun [au] (to surface of Sun)\n 8. Rsun (au)\n'\
             ' 9. dcMer [au] (to center of Mercury)\n10. dsMer [au] (to surface of Mercury)\n'\
             '11. tRhMer (3 x Rhill of Mercury) [au]\n12. Rmer [au]\n'\
             '13. dcVen [au] (to center of Venus)\n14. dsVen [au] (to surface of Venus)\n'\
             '15. tRhVen (3 x Rhill of Venus) [au]\n16. Rven [au]\n'\
             '17. dcEar [au] (to center of Earth)\n18. dsEar [au] (to surface of Earth)\n'\
             '19. tRhEar (3 x Rhill of Earth) [au]\n20. Rear [au]\n'\
             '21. dcMar [au] (to center of Mars)\n22. dsMar [au] (to surface of Mars)\n'\
             '23. tRhMar (3 x Rhill of Mars) [au]\n24. Rmar [au]\n'\
             '25. dcJup [au] (to center of Jupiter)\n26. dsJup [au] (to surface of Jupiter)\n'\
             '27. tRhJup (3 x Rhill of Jupiter) [au]\n28. Rjup [au]\n'\
             '29. dcSat [au] (to center of Saturn)\n30. dsSat [au] (to surface of Saturn)\n'\
             '31. tRhSat (3 x Rhill of Saturn) [au]\n32. Rsat [au]\n'\
             '33. dcUra [au] (to center of Uranus)\n34. dsUra [au] (to surface of Uranus)\n'\
             '35. tRhUra (3 x Rhill of Uranus) [au]\n36. Rura [au]\n'\
             '37. dcNep [au] (to center of Neptune)\n38. dsNep [au] (to surface of Neptune)\n'\
             '39. tRhNep (3 x Rhill of Neptune) [au]\n40. Rnep [au]\n'\
             '41. a [au]\n42. perihel, or a(1 - e) [au]\n43. e\n44. Porb [yr]\n45. KL (Kozai-Lidov parameter)\n'\
             '46. inc [deg]\n47. Omg, or Omega [deg]\n48. omg, or omega [deg]\n49. f (true anomaly) [deg]\n'\
             '50. E (energy, w/o unit)\n51. J (angular momentum, w/o unit)\n52. enc (encounter label, if any)\n'\
             '53. pln (name of encountered planet [and collision label], if any)\n')


    times     = np.linspace(0, Tint * 2 * np.pi, Nout)

    dpdist0                            = []
    dpdist1, dpdist2, dpdist3, dpdist4 = [], [], [], []
    dpdist5, dpdist6, dpdist7, dpdist8 = [], [], [], []

    # distance to surface of planets and Sun
    dpSdist0                               = []
    dpSdist1, dpSdist2, dpSdist3, dpSdist4 = [], [], [], []
    dpSdist5, dpSdist6, dpSdist7, dpSdist8 = [], [], [], []

    # encounter index
    idxEncSun, idxEncMer, idxEncVen, idxEncEar, idxEncMar = [], [], [], [], []

    encFacDist = 3
    E          = sim.energy()
    Jx, Jy, Jz = sim.angular_momentum()
    J          = np.sqrt(Jx*Jx + Jy*Jy + Jz*Jz)
    
    outdat.write('t,dt,x,y,z,dcSun,dsSun,Rsun,dcMer,dsMer,tRhMer,Rmer,dcVen,dsVen,tRhVen,Rven,dcEar,dsEar,tRhEar,Rear,dcMar,dsMar,tRhMar,Rmar,dcJup,dsJup,tRhJup,Rjup,dcSat,dsSat,tRhSat,Rsat,dcUra,dsUra,tRhUra,Rura,dcNep,dsNep,tRhNep,Rnep,a,perihel,e,Porb,KL,inc,Omg,omg,f,E,J,enc,pln\n')
    
    for l,time in enumerate(times):
        sim.integrate(time)

        dp0 = ps[-1] - ps[0]
        dp1 = ps[-1] - ps[1]
        dp2 = ps[-1] - ps[2]
        dp3 = ps[-1] - ps[3]
        dp4 = ps[-1] - ps[4]
        dp5 = ps[-1] - ps[5]
        dp6 = ps[-1] - ps[6]
        dp7 = ps[-1] - ps[7]
        dp8 = ps[-1] - ps[8]

        dist0 = np.sqrt(dp0.x * dp0.x + dp0.y * dp0.y + dp0.z * dp0.z)
        dist1 = np.sqrt(dp1.x * dp1.x + dp1.y * dp1.y + dp1.z * dp1.z)
        dist2 = np.sqrt(dp2.x * dp2.x + dp2.y * dp2.y + dp2.z * dp2.z)
        dist3 = np.sqrt(dp3.x * dp3.x + dp3.y * dp3.y + dp3.z * dp3.z)
        dist4 = np.sqrt(dp4.x * dp4.x + dp4.y * dp4.y + dp4.z * dp4.z)
        dist5 = np.sqrt(dp5.x * dp5.x + dp5.y * dp5.y + dp5.z * dp5.z)
        dist6 = np.sqrt(dp6.x * dp6.x + dp6.y * dp6.y + dp6.z * dp6.z)
        dist7 = np.sqrt(dp7.x * dp7.x + dp7.y * dp7.y + dp7.z * dp7.z)
        dist8 = np.sqrt(dp8.x * dp8.x + dp8.y * dp8.y + dp8.z * dp8.z)
    
        sdist0 = dist0 - list(major_bodies_radius.values())[0]/au
        sdist1 = dist1 - list(major_bodies_radius.values())[1]/au
        sdist2 = dist2 - list(major_bodies_radius.values())[2]/au
        sdist3 = dist3 - list(major_bodies_radius.values())[3]/au
        sdist4 = dist4 - list(major_bodies_radius.values())[4]/au
        sdist5 = dist5 - list(major_bodies_radius.values())[5]/au
        sdist6 = dist6 - list(major_bodies_radius.values())[6]/au
        sdist7 = dist7 - list(major_bodies_radius.values())[7]/au
        sdist8 = dist8 - list(major_bodies_radius.values())[8]/au

        dpdist0.append(dist0)
        dpdist1.append(dist1)
        dpdist2.append(dist2)
        dpdist3.append(dist3)
        dpdist4.append(dist4)
        dpdist5.append(dist5)
        dpdist6.append(dist6)
        dpdist7.append(dist7)
        dpdist8.append(dist8)
    
        dpSdist0.append(sdist0)
        dpSdist1.append(sdist1)
        dpSdist2.append(sdist2)
        dpSdist3.append(sdist3)
        dpSdist4.append(sdist4)
        dpSdist5.append(sdist5)
        dpSdist6.append(sdist6)
        dpSdist7.append(sdist7)
        dpSdist8.append(sdist8)

        kl = np.sqrt(1 - ps[-1].e**2)*(np.cos(ps[-1].inc))
    
        rhillPl = np.zeros(N - 2)
    
        for j in range(1, N - 1):
            rhillPl[j - 1]   = encFacDist * ps[j].a * np.cbrt(ps[j].m/3/ps[0].m)
    
        #or dist5 <= rhillPl[4] or dist6 <= rhillPl[5] or dist7 <= rhillPl[6] or dist8 <= rhillPl[7]:
        nameB = ''
        if (sdist0/(list(major_bodies_radius.values())[0]/au)) <= 0.01 or dist1 <= rhillPl[0] or dist2 <= rhillPl[1] or dist3 <= rhillPl[2] or dist4 <= rhillPl[3]:
            label = 'ENC'
            if (sdist0/(list(major_bodies_radius.values())[0]/au)) <= 0.01:
                idxEncSun.append(i)
                nameB += list(major_bodies.items())[0][1]+' '+'+COL'
            if dist1 <= rhillPl[0]:
                idxEncMer.append(i)
                if (sdist1/(list(major_bodies_radius.values())[1]/au)) <= 0.01:
                    nameB += list(major_bodies.items())[1][1]+' '+'+COL'
                else:
                    nameB += list(major_bodies.items())[1][1]+' '
            if dist2 <= rhillPl[1]:
                idxEncVen.append(i)
                if (sdist2/(list(major_bodies_radius.values())[2]/au)) <= 0.01:
                    nameB += list(major_bodies.items())[2][1]+' '+'+COL'
                else:
                    nameB += list(major_bodies.items())[2][1]+' '
            if dist3 <= rhillPl[2]:
                idxEncEar.append(i)
                if (sdist3/(list(major_bodies_radius.values())[3]/au)) <= 0.01:
                    nameB += list(major_bodies.items())[3][1]+' '+'+COL'
                else:
                    nameB += list(major_bodies.items())[3][1]+' '
            if dist4 <= rhillPl[3]:
                idxEncMar.append(i)
                if (sdist4/(list(major_bodies_radius.values())[4]/au)) <= 0.01:
                    nameB += list(major_bodies.items())[4][1]+' '+'+COL'
                else:
                    nameB += list(major_bodies.items())[4][1]+' '
        else:
            label = '   '
        
        outdat.write(f'{time/2/np.pi:8.3f},{sim.dt/2/np.pi:6.3f},'\
              f'{ps[9].x:+10.6f},{ps[9].y:+10.6f},{ps[9].z:+10.6f},'\
              f'{dist0:11.9f},{sdist0:11.9f},{list(major_bodies_radius.values())[0]/au:11.9f},'\
              f'{dist1:11.9f},{sdist1:11.9f},{rhillPl[0]:11.9f},{list(major_bodies_radius.values())[1]/au:11.9f},'\
              f'{dist2:11.9f},{sdist2:11.9f},{rhillPl[1]:11.9f},{list(major_bodies_radius.values())[2]/au:11.9f},'\
              f'{dist3:11.9f},{sdist3:11.9f},{rhillPl[2]:11.9f},{list(major_bodies_radius.values())[3]/au:11.9f},'\
              f'{dist4:11.9f},{sdist4:11.9f},{rhillPl[3]:11.9f},{list(major_bodies_radius.values())[4]/au:11.9f},'\
              f'{dist5:11.9f},{sdist5:11.9f},{rhillPl[4]:11.9f},{list(major_bodies_radius.values())[5]/au:11.9f},'\
              f'{dist6:11.9f},{sdist6:11.9f},{rhillPl[5]:11.9f},{list(major_bodies_radius.values())[6]/au:11.9f},'\
              f'{dist7:11.9f},{sdist7:11.9f},{rhillPl[6]:11.9f},{list(major_bodies_radius.values())[7]/au:11.9f},'\
              f'{dist8:11.9f},{sdist8:11.9f},{rhillPl[7]:11.9f},{list(major_bodies_radius.values())[8]/au:11.9f},'\
              f'{ps[9].a:11.9f},{ps[9].a*(1 - ps[9].e):11.9f},{ps[9].e:8.6f},{ps[9].P/2/np.pi:10.6f},{kl:12.9f},'\
              f'{180*ps[9].inc/np.pi:6.1f},{180*ps[9].Omega/np.pi:6.1f},{180*ps[9].omega/np.pi:6.1f},'\
              f'{180*ps[9].f/np.pi:6.1f},'\
              f'{E:8.6E},{J:8.6E},{label:3},{nameB}\n')
    
    outlog.write(f'*** Simulation #{i+1:03d}/{len(combi):03d} w/ combination {combi[i]} done. '\
                 f'Finish at {datetime.now()}...\n')

    print(f'NOTE: *** Close encounter index ***\n'\
      f'{list(major_bodies.items())[0][1]:<7}: {idxEncSun}\n'\
      f'{list(major_bodies.items())[1][1]:<7}: {idxEncMer}\n'\
      f'{list(major_bodies.items())[2][1]:<7}: {idxEncVen}\n'\
      f'{list(major_bodies.items())[3][1]:<7}: {idxEncEar}\n'\
      f'{list(major_bodies.items())[4][1]:<7}: {idxEncMar}')
    outlog.write(f'NOTE: *** Close encounter index ***\n'\
      f'{list(major_bodies.items())[0][1]:<7}: {idxEncSun}\n'\
      f'{list(major_bodies.items())[1][1]:<7}: {idxEncMer}\n'\
      f'{list(major_bodies.items())[2][1]:<7}: {idxEncVen}\n'\
      f'{list(major_bodies.items())[3][1]:<7}: {idxEncEar}\n'\
      f'{list(major_bodies.items())[4][1]:<7}: {idxEncMar}\n')
    
    outdat.close()
    outlog.close()
    
    times, ps, sim = None, None, None
