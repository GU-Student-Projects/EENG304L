# Plot_LTSim.py
from PyLTSpice import RawRead
import matplotlib.pyplot as plt
import numpy as np


LTR = RawRead("./2_ee303L_modified.raw") 

print(LTR.get_trace_names())
print("\n")
print(LTR.get_raw_property())
print("\n")
steps = LTR.get_steps()
num_steps = len(steps) 
print('number of sweeps in the simulation:', num_steps)


# objects containing the data
f = LTR.get_trace('frequency')
Vo = LTR.get_trace('v(out)')

# extract the data from the objects
if num_steps == 1:
   freq = f.get_wave(0)
   Vout = Vo.get_wave(0)


# compute midband gain and cut-off frequency
mag = 20*np.log10(abs(Vout))
midgain_dB = max(mag)
print("\nmidband gain: %.3f" %midgain_dB, " (dB)")
tupla = np.where(mag <= midgain_dB-3)
ind = tupla[-1][-1] # get the last value of the tupla
fL = abs(freq[ind]) 
f_L = "low frequency cut off = %.3f (Hz)" % fL
print(f_L)

str_1 = "midband gain = %.2f (dB)" %(midgain_dB)
str_2 = "$f_L$ = %.2f (Hz)" %fL

# Plot the Simulation
fig1 = plt.figure()      

plt.subplot(211) # 2 plots - col 1, row 1
plt.grid(True, which="both", axis="x")
plt.title("Frequency response (magnitude)" )
plt.ylabel("Magnitude (dB)")
plt.xlabel("frequency (Hz)")

plt.semilogx(freq, mag)
plt.xlim((1e-1,1e5))
plt.ylim((3,13))
plt.annotate(str_1+'\n'+str_2, xy=(1e2,8),ha='left', va='top',
                color='tab:purple')


plt.subplot(212) # 2 plots - plot col 1, row 2
plt.grid(True, which="both", axis="x")
plt.title("Frequency response (phase)" )
plt.ylabel("Phase (${\\circ}$)")
plt.xlabel("frequency (Hz)")
ph = np.angle(Vout, deg=True)
plt.semilogx(freq, ph)
plt.xlim((1e-1,1e5)) 
plt.ylim((-180,-120))
plt.yticks(np.arange(-180,-110, step=10)) 

fig1.tight_layout()
plt.show()