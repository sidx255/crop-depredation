#final

import wave
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "Z:/wav/3.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* Recording *")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print('Audio recorded')        

ifile = wave.open('Z:/wav/crow 3.wav')
ifile1 = wave.open(WAVE_OUTPUT_FILENAME)

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

audio_normalised.resize(audio_normalised_1.size)
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