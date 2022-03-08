from pydub import AudioSegment

song = AudioSegment.from_wav("Z:/Siddharth/Drive/wav/crow 1.wav")
two_seconds=2 * 1000
song = song[:two_seconds]
song = song.set_frame_rate(16000)
song.export("Z:/Siddharth/Drive/wav/1.wav", format="wav")
song1 = AudioSegment.from_wav("Z:/Siddharth/Drive/wav/crow 3.wav")
song1 = song1[:two_seconds]
song1 = song1.set_frame_rate(16000)
song1.export("Z:/Siddharth/Drive/wav/2.wav", format="wav")