#5_heatmap_selfCorrelation.py

import wave
import numpy as np
import matplotlib.pyplot as plt

# Read file to get buffer                                                                                               
ifile1 = wave.open('Z:/Siddharth/Drive/wav/crow 3.wav')
samples1 = ifile1.getnframes()
audio1 = ifile1.readframes(samples1)

ifile = wave.open('Z:/Siddharth/Drive/wav/crow 1.wav')
samples = ifile.getnframes()
audio = ifile.readframes(samples)

# Convert buffer to float32 using NumPy                                                                                 
audio_as_np_int16 = np.frombuffer(audio1, dtype=np.int8)
audio_as_np_float32 = audio_as_np_int16.astype(np.float32)

audio_as_np_int16x = np.frombuffer(audio, dtype=np.int8)
audio_as_np_float32x = audio_as_np_int16x.astype(np.float32)


# Normalise float32 array so that values are between -1.0 and +1.0                                                      
max_int16 = 2**15

audio_normalised = audio_as_np_float32 / max_int16
print(audio_normalised)

audio_normalised1= audio_as_np_float32x / max_int16
print(audio_normalised1)

corr_matrix = np.corrcoef(audio_normalised,audio_normalised).round(decimals=2)
print(corr_matrix)


#to plot heatmap of correlation

fig, ax = plt.subplots()
im = ax.imshow(corr_matrix)
im.set_clim(-1, 1)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('x','y'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('x','y'))
ax.set_ylim(1.5,-0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, corr_matrix[i, j], ha='center', va='center',color='r')
cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
plt.show()