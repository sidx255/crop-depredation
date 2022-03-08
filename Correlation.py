import numpy as np
import wave
import matplotlib.pyplot as plt

wfp = wave.open('C:/Users/Hp/Prototype/crow 4.wav', 'rb')
samples = wfp.readframes(wfp.getnframes())
signal = np.frombuffer(samples, np.int16)
corr = np.correlate(signal, signal, "full")
signal = signal / float(0xFFFF)
print(signal)
plt.plot(signal[0:1024])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()