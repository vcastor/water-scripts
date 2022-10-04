#!/opt/homebrew/bin/python3
#This script write a new xyz file, ordening the H2O molecules
#as OHH, OHH, OHH,...
import sys
import os
import numpy as np

def distance(xyz1, xyz2):
    x1, x2 = xyz1[0], xyz2[0]
    y1, y2 = xyz1[1], xyz2[1]
    z1, z2 = xyz1[2], xyz2[2]
    x1, x2 = float(x1), float(x2)
    y1, y2 = float(y1), float(y2)
    z1, z2 = float(z1), float(z2)
    d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
    #d = np.sqrt(d)
    #It's not necessary at all compute the distance, the square works in this case
    return d

fdesorden = sys.argv[1]
archivo = open(fdesorden, 'r')
datadesorden = archivo.readlines()

nsize = len(datadesorden) - 2
n = datadesorden[0]
n = int(n)

oxs = []
hys = []

if (not(nsize == n)):
    print("something isn't ok in the xyz file")

for i in range(n):
    linen = datadesorden[i+2]
    linen = linen.split()
    if (linen[0] == 'O'):
        oxs.append(linen[1:4])
    elif (linen[0] == 'H'):
        hys.append(linen[1:4])

disOH = []
Hord  = []
for i in range(n//3):
    for j in range(2*n//3):
        disOH.append(distance(oxs[i][:], hys[j][:]))
    newdis = sorted(disOH)
    for j in range(2*n//3):
        if (disOH[j] == newdis[0] or disOH[j] == newdis[1]):
            Hord.append(hys[j])
    disOH.clear()

for i in range(n//3):
    oxs[i][:] = float(oxs[i][0]), float(oxs[i][1]), float(oxs[i][2])
for i in range(2*n//3):
    Hord[i][:] = float(Hord[i][0]), float(Hord[i][1]), float(Hord[i][2])

print(n)
print("")
j = 0
for i in range(n//3):
    print('O    ', '{:+.8f}'.format(oxs[i][0]), '  ', '{:+.8f}'.format(oxs[i][1]), '  ', '{:+.8f}'.format(oxs[i][2]))
    print('H    ', '{:+.8f}'.format(Hord[j][0]), '  ', '{:+.8f}'.format(Hord[j][1]), '  ', '{:+.8f}'.format(Hord[j][2]))
    j += 1
    print('H    ', '{:+.8f}'.format(Hord[j][0]), '  ', '{:+.8f}'.format(Hord[j][1]), '  ', '{:+.8f}'.format(Hord[j][2]))
    j += 1
