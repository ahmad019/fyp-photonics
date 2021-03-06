# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 17:05:55 2019

@author: ahmad

Add drop micro ring resonator equations as from fabry perot assymetric
"""


import numpy as np
import matplotlib.pyplot as plt

ran = 200
phi = -1
r1 = 0.9998
r2 = 0.9889
c = 299792458
lamd = 0.000001550
Q1 = 5000000
Q2 = 6000000
b = 0.000025
l = 2*np.pi*b
n = 3.45

aa = (2*np.pi*n)/(Q1*lamd)
g1 = 500
aa2 = (2*np.pi*n)/(Q2*lamd)
g2 = 500

a1 = np.exp(-(aa-g1)*l/2)
a2 = np.exp(-(aa2-g2)*l/2)

#r1 = r2*a1

t = np.sqrt(1-(r1**2))
t2 = np.sqrt(1-(r2**2))


Etai = np.ndarray(ran, float)
Erai = np.ndarray(ran, float)
PHIt = np.ndarray(ran, float)
PHIr = np.ndarray(ran, float)
phit = np.ndarray(ran, float)
dPHIr = np.ndarray(ran, float)

for i in range(0,ran):
    
    Eta = (r1-a1*r2*np.exp(1j*phi))/(1-a1*r1*r2*np.exp(1j*phi)) #asymmeteric transmission
    
    Era = -(t*t2*np.exp(1j*phi/2))/(1-r1*r2*np.exp(1j*phi)) #asymmeteric reflection

    PHIt[i] = phi/2    
    PHIr[i] = np.arctan((a1*r1*np.sin(phi))/(1-a1*r1*np.cos(phi))) - np.arctan((a1*np.sin(phi))/(r1-a1*np.cos(phi)))
    #PHIr[i] = np.arctan((r1*np.sin(phi))/(1-r1*np.sin(phi))) - np.arctan(np.sin(phi)/(r1-np.cos(phi))) #singapore paper phase
    
    
    phi = phi + 0.01    
    
    Etai[i] = abs(Eta)**2 #abs(Eta*EtaC)
    Erai[i] = abs(Era)**2 #abs(Era*EraC)
    
    dPHIr[i] = ((r1-r2*np.cos(phi))**2/((r1-r2*np.cos(phi))**2 + (r2*np.sin(phi))**2))  - ((1-r1*r2*np.cos(phi))**2 / ((1-r1*r2*np.cos(phi))**2  + (r1-r2*np.sin(phi))**2))
    
    phit[i] = phi

dPHIt = 1/2
#dPHIr = ((r1-r2*np.cos(phi))**2/((r1-r2*np.cos(phi))**2 + (r2*np.sin(phi))**2))  + ((1-r1*r2*np.cos(phi))**2 / ((1-r1*r2*np.cos(phi))**2  + (r1-r2*np.sin(phi))**2))
#dPHIr = ((1-r1*np.sin(phi))**2/((1-r1*np.sin(phi))**2 + (np.sin(phi))**2))  + ((r1-np.cos(phi))**2 / ((r1-np.cos(phi))**2  + (np.sin(phi))**2)) #singapore paper phase derivt

phit = phit.round(decimals=4)

vgt = (2*c)/n
ngt = n/2

vgr = (1/dPHIr)*c/n
ngr = dPHIr * n

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,4))

axs[0].set_title("Reflection")
axs[0].set_xlabel("Round Trip phase")
axs[0].set_ylabel("Intensity")
#axs[0].plot(phit,Etai, 'b')
axs[0].plot(phit,Erai, 'r')


axs[1].set_title("Transmission")
axs[1].set_xlabel("Round trip phase")
axs[1].set_ylabel("Intensity")
axs[1].plot(phit,Etai, 'b')

#fig2, axs = plt.subplots(1)

#axs.set_xlim([-0.2,0.2])
#axs.set_title("Reflection Phase")
#axs.set_xlabel("detuning")
#axs.set_ylabel("Effective phase")
#axs.plot(phit,PHIr, 'r')


fig.tight_layout()
#fig2.tight_layout()
plt.show()

#plt.xlim([-0.25,0.25])
#plt.plot(phit, vgr, 'b')
#plt.show()

fig.savefig('add_drop_fabry.png', dpi=400)
#fig2.savefig('add_drop_fabry(phase).png', dpi=400)
