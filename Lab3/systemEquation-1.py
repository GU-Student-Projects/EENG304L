#!/usr/bin/env python3
"""
Example showing how to solve systems of equations with Python
@author: claudio
Filename: systemEquation.py
"""
import sympy as sp

VG = 1.5
VT = 0.5
KP = 50e-6
W_L = 20/2
RS = 1000

ID, VS = sp.symbols('ID VS')

eq1 = sp.Eq(ID - 0.5*KP*W_L*(VG - VS - VT)**2, 0)
eq2 = sp.Eq(VS - ID*RS, 0)

sol = sp.solve([eq1, eq2],ID,VS,dict=True)
print(sol)

# check if the solutions are feasible 
val = list(sol[0].values())
if (VG - val[1] > VT):
    a = val[0]*1e6 
    print("ID = %.2f uA" % a)

val = list(sol[1].values())
if (VG - val[1] > VT):
    a = val[0]*1e6 
    print("ID = %.2f uA" % a)
