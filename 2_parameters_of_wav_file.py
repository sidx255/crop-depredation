import wave
obj = wave.open('C:/Users/siddh/Desktop/wav/crow distress.wav','rb')
print( "Number of channels=",obj.getnchannels())
print ( "Sample width=",obj.getsampwidth())
print ( "Frame rate=",obj.getframerate())
print ("Number of frames=",obj.getnframes())
print ( "parameters:",obj.getparams())
obj.close()