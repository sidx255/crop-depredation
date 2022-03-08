import os
import librosa
from librosa import feature
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import pandas as pd
from playsound import playsound
import warnings
warnings.filterwarnings("ignore")

fn_list_i = [
 feature.chroma_stft,
 feature.spectral_centroid,
 feature.spectral_bandwidth,
 feature.spectral_rolloff
]

fn_list_ii = [
    feature.rms,
 feature.zero_crossing_rate
]

def get_feature_vector(y,sr):
   feat_vect_i = [ np.mean(funct(y,sr)) for funct in fn_list_i]
   feat_vect_ii = [ np.mean(funct(y)) for funct in fn_list_ii]
   feature_vector = feat_vect_i + feat_vect_ii
   return feature_vector

duration = 3
fs = 48000
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
print("Recording Audio")
sd.wait()

sd.play(myrecording,fs)
print("Playingback Audio")

sd.wait()
write('/home/pi/py codes/test/record.wav', fs, myrecording)
print("Audio Saved")

index = {}
votes={}
directory = r"/home/pi/py codes/test"
for entry in os.scandir(directory):
    if (entry.is_file()):
        index[entry.path[23:28]]=entry.path
        votes[entry.path[23:27]]=0
df=pd.DataFrame(columns=['Bird','A','B','C','D','E','F'])

for i in index.keys():
    audio_data = index[i]
    y , sr = librosa.load(audio_data,sr=None)
    feature_vector = get_feature_vector(y, sr)
    print(i,feature_vector)
    ########################
    feature_vector.insert(0,i[0:4])
    tempSeries=pd.Series(feature_vector,index=['Bird','A','B','C','D','E','F'])
    df=df.append(tempSeries,ignore_index=True)



#Machine Learning##############
print("\n\n------ML Results------")
# Importing the dataset
X_train= df.iloc[:len(df.index)-1, 1:].values
Y_train = df.iloc[:len(df.index)-1,0].values

recorded= df.iloc[len(df.index)-1:len(df.index), 1:].values


#KNN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 3, metric = 'minkowski', p = 2)
classifier.fit(X_train, Y_train)
knn_pred = classifier.predict(recorded)[0]
print("KNN Result :",knn_pred)
votes[knn_pred]=votes[knn_pred]+1


#Random forest
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 3, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, Y_train)
rf_result = classifier.predict(recorded)[0]
print("Random Forest Result :",rf_result)
votes[rf_result]=votes[rf_result]+1


#Naive_bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)
nb_result = classifier.predict(recorded)[0]
print("Naive Bayes result :",nb_result)
votes[nb_result]=votes[nb_result]+1

#Kernel SVM
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, Y_train)
ksvm_result = classifier.predict(recorded)[0]
print("Kernel SVM result :",ksvm_result)
votes[ksvm_result]=votes[ksvm_result]+1

#Decision Tree
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, Y_train)
dt_result = classifier.predict(recorded)[0]
print("Decision Tree result :",dt_result)
votes[dt_result]=votes[dt_result]+1
#################################################

audio_data = index['recor']
y , sr = librosa.load(audio_data,sr=None)
reco_vector = get_feature_vector(y, sr)

print("\n\n-----Subtraction Algo result-----")

sub_result = "None"
least=9999
for i in index.keys():
    audio_data = index[i]
    y , sr = librosa.load(audio_data,sr=None)
    feature_vector = get_feature_vector(y, sr)
    net=0
    for j in range(0,5):
        net=net+abs(feature_vector[j]-reco_vector[j])
    if net<least and net!=0:
        sub_result=i
        least=net
    print(i,net)
print("The bird is ",sub_result)
votes[sub_result[0:4]]=votes[sub_result[0:4]]+1

print("\n---Final Vote Count---")
print(votes)

max_votes=max(votes, key=votes.get)

print("Bird Ditected : "+max_votes)

playsound('/home/pi/py codes/test/Distress Calls/'+max_votes+'.wav')
