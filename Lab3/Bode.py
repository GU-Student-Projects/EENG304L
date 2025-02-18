# Bode.py
import numpy as np
import matplotlib.pyplot as plt
import control as ct

s = ct.tf('s')
N = 100*(1 + s/1)
D = (1 + s/10) * (1 + s/100)
sys = N / D

print(sys)

A0 = ct.dcgain(sys) # DC gain
poles = ct.poles(sys)
zeros = ct.zeros(sys)

print("DC gain is:",A0)
print("poles are:", poles)
print("zeros are;", zeros)

ct.bode_plot(sys,dB=True,Hz=True,title="Frequency Response",wrap_phase=True)
plt.show()

ct.pole_zero_plot(sys,title="Pole/zero plot")
plt.show()

# customize the plots
mag, phase, omega = ct.frequency_response(sys)
magdb = 20*np.log10(abs(mag))
plt.figure(1)
plt.semilogx(omega, magdb, label='Magnitude (dB)')
plt.grid(which='both', axis = 'both')
plt.legend()
plt.xlabel('$\\omega$ (rad/s)')
str = '$T(s) = 100 \\cdot $' + \
          '$\\dfrac{1+s}{(1+\\dfrac{s}{10}) \\cdot (1 + \\dfrac{s}{100})}$'
plt.title(str)
plt.show()
