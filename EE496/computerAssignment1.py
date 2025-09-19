# -*- coding: utf-8 -*-
"""
Kevin Morales

Computer Assigment 1
"""

import numpy as np

n = np.arange(-9999,1000,2) # by running with 1 spacing, there are only odd harmonics

#Dn derived on handwritten notes
Dn = (1 / (2j*np.pi*n)) * (-2*np.exp(-0.5j*np.pi*n) + np.exp(0.5j*np.pi*n) + np.exp(-1.5j*np.pi*n))
AbsDn = np.abs(Dn)
PowerPerCoeff = AbsDn **2
#total Power = 1
# cumulative power = fraction of total power

#Arrays sorted around to accoutn for BW being calculated outward from 0
sortedIndices = np.argsort(np.abs(n))
sorted_n = n[sortedIndices]
sortedPower = PowerPerCoeff[sortedIndices]
cumulativePower = np.cumsum(sortedPower)

#Finding the index and corresponding harmonic with the right accumulated power
harmonic95location = np.argmax(cumulativePower >= 0.95)
harmonic95 = sorted_n[harmonic95location]
harmonic99location = np.argmax(cumulativePower >= 0.99)
harmonic99 = sorted_n[harmonic99location]

f0 = 1/4
# n * f0 = fn
BWPower95 = abs(harmonic95) * f0
BWPower99 = abs(harmonic99) * f0

print(f"BW of 95% power: {BWPower95:.3f} Hz") # 2.250 Hz
print(f"BW of 99% power: {BWPower99:.3f} Hz") # 10.250 Hz




