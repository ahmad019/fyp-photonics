# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:45:46 2018

@author: ahmad
"""

import numpy as np
import matplotlib.pyplot as plt

ran = 200
phi = -1
r = 0.98797
r2 = 0.97889

t = np.sqrt(1-(r**2))
t2 = np.sqrt(1-(r2**2))


Etai = np.ndarray(ran, float)
Erai = np.ndarray(ran, float)
Ersi = np.ndarray(ran, float)
phit = np.ndarray(ran, float)

for i in range(0,ran):
    
    Era = (r-r2*np.exp(1j*phi))/(1-r*r2*np.exp(1j*phi)) #asymmeteric reflection
    
    Eta = -(t*t2*np.exp(1j*phi/2))/(1-r*r2*np.exp(1j*phi)) #asymmeteric transmission

    
    phi = phi + 0.01    
    
    Etai[i] = abs(Eta)**2 #abs(Eta*EtaC)
    Erai[i] = abs(Era)**2 #abs(Era*EraC)
    Ersi[i] = Etai[i] + Erai[i]
    phit[i] = phi

#plt.xlim([-1,1])
#plt.ylim([-0.2,1.2])
#plt.legend(Eta,Ets, borderpad=2)
#plt.legend([Etai, Etsi], ["line 2", "line 1"])

plt.title('Reflection + Transmission Fabry-Perot Resonator')
plt.xlabel('Round Trip Phase "Φ"')
plt.ylabel('Intensity')

plt.plot(phit,Etai, 'b') #transmittance
plt.plot(phit,Erai, 'r') #reflectance

plt.show()

plt.title('Reflection + Transmission Intensity')
plt.plot(phit,Ersi, 'y')
plt.show
