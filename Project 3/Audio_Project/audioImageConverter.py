import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

#import libraries
import os
import matplotlib.pyplot as plt
import librosa
import librosa.display
import scipy.signal as sg
import numpy as np

def filterBySample(signal, sample, cut_by_max=False, percent_mean=0.7, max_noise = 0.15, default_noise=0.1):
    #print(len(signal))
    signal_sample = signal[sample[0]:sample[1]]
    signal_sample = signal_sample[signal_sample > 0]
    signal_sample = abs(signal_sample)
    noise_mean = signal_sample.mean()
    if(not(cut_by_max)):
        signal_sample = signal_sample[signal_sample > (noise_mean + noise_mean*percent_mean)]
        noise_mean = signal_sample.mean()
    else:
        noise_mean = signal_sample.max()
    

    if (noise_mean > max_noise):
        noise_mean = default_noise
    
    #noise_mean = 1

    for x in np.nditer(signal, op_flags=['readwrite']) :
        if(x < 0):
            if(noise_mean < abs(x)):
                x += noise_mean
            else:
                x *= 0
            #print(x)
        else:
            if(x > noise_mean):
                x -= noise_mean
            else:
                x *= 0
    return signal
    
def lowPass(signal):
    # First, design the Buterworth filter
    N  = 5    # 3, 4 Filter order
    Wn = 0.08 # 0.1 Cutoff frequency
    B, A = sg.butter(N, Wn, output='ba')
    signal = sg.filtfilt(B,A, signal)
    return signal

def normalize(signal,pre_emphasis= 0.97):
    emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
    return emphasized_signal

def run():
    #path directory
    spectroPath = "Spectrogram"
    audio_fpath = "19316050-project3"
    
    for _file in os.listdir(audio_fpath):

        if not _file.endswith('.mp3'):
            continue

        fileName = _file.split('.')[0]
        X, sr = librosa.load(os.path.join(audio_fpath,_file), sr=44100)

        X = lowPass(X)
        X = normalize(X)
        X = filterBySample(X, [1,200],cut_by_max=True)

        # Convert the audio waveform to spectrogram
        X = librosa.stft(X)
        Xdb = librosa.amplitude_to_db(abs(X))
        plt.figure(figsize=(0.8, 0.8))
        plt.subplots_adjust(left=0,right=1,bottom=0,wspace=0,hspace=0) 
        plt.box(False)
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log',cmap='gray_r')
        plt.savefig(os.path.join(spectroPath,fileName+'.png'), bbox_inches=None, pad_inches=0)
        plt.close()


if __name__ == "__main__":
    run()    
	