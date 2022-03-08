import wave
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME ="home/pi/wav/reco.wav"
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


print('Audio recorded, now Correlating : ')   

def correlate(i,j):
    ifile = wave.open(i)
    ifile1 = wave.open(j)
    
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
    
    audio_normalised.resize(audio_normalised_1.size)
    corr_matrix = np.corrcoef(audio_normalised, audio_normalised_1).round(decimals=7)
    
    return(corr_matrix[0,1])


index = {}
directory = r'home/pi/wav'
for entry in os.scandir(directory):
    if (entry.is_file()):
        index[entry.path[30:34]]=entry.path
        
#for i in index.keys():
#    print(i,index[i])

for i in index.keys():
    if i=="reco":
        for j in index.keys():
            print(i,j,correlate(index[i],index[j]))
