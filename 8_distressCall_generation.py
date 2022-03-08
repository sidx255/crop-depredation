#if species identified correctly

from playsound import playsound

bird_identified=input('ENTER THE IDENTIFIED BIRD-')
bird_identified=bird_identified.lower()

if (bird_identified=='crow'):
    print('The audio generated will shoo the bird away')
    playsound('C:/Users/Hp/Prototype/crow distress.wav')
    
elif(bird_identified=='pigeon'):
    print('The audio generated will shoo the bird away')
    playsound('C:/Users/Hp/Prototype/pigeon distress.wav')
    
elif(bird_identified=='sparrow'):
    print('The audio generated will shoo the bird away')
    playsound('C:/Users/Hp/Prototype/sparrow distress.wav')
    
else:
    print('Distress call not found for the identified species')
    