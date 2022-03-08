#import wave
import numpy as np
#import matplotlib.pyplot as plt
import scipy.fftpack as fftpack
from scipy.io.wavfile import read

def similarity(template, test):
    corr = fftpack.irfft(fftpack.rfft(test , 2 * test.size ) *    
           fftpack.rfft(template[:-1] , 2 * template.size ))           

    return max(abs(corr)).round(decimals=2)

input_data = read("C:/Users/Hp/Prototype/pigeon 2.wav")
x= input_data[1]
input_data1= read("C:/Users/Hp/Prototype/sparrow 1.wav")
y= input_data1[1]

# Convert buffer to float32 using NumPy                                                                                 
audio_as_np_int16 = np.frombuffer(x, dtype=np.int8)
audio_as_np_float32 = audio_as_np_int16.astype(np.float32)

audio_as_np_int16x = np.frombuffer(y, dtype=np.int8)
audio_as_np_float32x = audio_as_np_int16x.astype(np.float32)

# Normalise float32 array so that values are between -1.0 and +1.0                                                      
max_int16 = 2**15

audio_normalised = audio_as_np_float32 / max_int16
print(audio_normalised)

audio_normalised1= audio_as_np_float32x / max_int16
print(audio_normalised1)

corr_matrix = np.corrcoef(audio_normalised,audio_normalised1).round(decimals=2)
print(corr_matrix)


t=similarity(x,y) 
print(t)

