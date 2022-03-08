#6_correlation.py

import wave
import numpy as np
import matplotlib.pyplot as plt

def corr2_coeff(A, B):
    # Rowwise mean of input arrays & subtract from input arrays themeselves
    A_mA = A - A.mean(1)[:, None]
    B_mB = B - B.mean(1)[:, None]

    # Sum of squares across rows
    ssA = (A_mA**2).sum(1)
    ssB = (B_mB**2).sum(1)

    # Finally get corr coeff
    return np.dot(A_mA, B_mB.T) / np.sqrt(np.dot(ssA[:, None],ssB[None]))

# Read file to get buffer for audio 1                                                                                            
ifile = wave.open('Z:/Siddharth/Drive/wav/crow 1.wav')
ifile1 = wave.open('Z:/Siddharth/Drive/wav/pigeon 1.wav')

samples = ifile.getnframes()
samples1 = ifile1.getnframes()

audio = ifile.readframes(samples)
audio1 = ifile1.readframes(samples1)

# Convert buffer to float32 using NumPy                                                                                 
audio_as_np_int16 = np.frombuffer(audio, dtype=np.int8)
audio_as_np_int16_1 = np.frombuffer(audio1, dtype=np.int8)

audio_as_np_float32 = audio_as_np_int16.astype(np.float32)
audio_as_np_float32_1 = audio_as_np_int16_1.astype(np.float32)

# Normalise float32 array so that values are between -1.0 and +1.0                                                      
max_int16 = 2**15

audio_normalised = audio_as_np_float32 / max_int16
audio_normalised_1 = audio_as_np_float32_1 / max_int16

print(audio_normalised)
print(audio_normalised_1)

audio_normalised_1.resize(audio_normalised.size)
corr_matrix = np.corrcoef(audio_normalised, audio_normalised_1).round(decimals=7)
print(corr_matrix)

#to plot heatmap of correlation

fig, ax = plt.subplots()
im = ax.imshow(corr_matrix)
im.set_clim(-1, 1)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1, 2), ticklabels=('x', 'y', 'z'))
ax.yaxis.set(ticks=(0, 1, 2), ticklabels=('x', 'y', 'z'))
ax.set_ylim(2.5, -0.5)
for i in range(len(corr_matrix)):
    for j in range(len(corr_matrix[0])):
        ax.text(j, i, corr_matrix[i, j], ha='center', va='center',
                color='r')
cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
plt.show()