#In[]:
import pygame
import pygame as pg
def play_music(music_file):
    '''
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    '''
    clock = pg.time.Clock()
    try:
      pg.mixer.music.load(music_file)
      print("Music file {} loaded!".format(music_file))
    except pygame.error:
        print("File {} not found! {}".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    # check if playback has finished
    while pg.mixer.music.get_busy():
        clock.tick(30)
# pick a midi or MP3 music file you have in the working folder
# or give full pathname
music_file = input("Please input the midi file path:")
#music_file = "Drumtrack.mp3"
freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 2048  # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pg.mixer.music.set_volume(0.8)
try:
    play_music(music_file)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pg.mixer.music.fadeout(1000)
    pg.mixer.music.stop()
    raise SystemExit

#In[]: 读取文件
import midi
from scipy.io import wavfile 
import os
audio_root = '/data2/process_data/caojihua/data/MedleyDB/MedleyDB_sample/Audio'
example_file = 'LizNelson_Rainfall/LizNelson_Rainfall_STEMS/LizNelson_Rainfall_STEM_01.wav'
sample_rate, sig = wavfile.read(os.path.join(audio_root, example_file))

#In[]: 显示波形图
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, sig.shape[0] - 1, num=sig.shape[0], dtype=np.int64)
plt.subplot(211)
plt.plot(t, sig.T[0])
plt.subplot(212)
plt.plot(t, sig.T[1])
plt.show()

#In[]: 显示子集波形图
start = 1000
len = 9000000
plt.plot(list(range(start, start + len)), sig.T[0][start: start + len])

#In[]: 显示时频分析
from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 600
f, t, sxx = signal.spectrogram(sig.T[0][1: 10000], fs=sample_rate)
print(f.shape)
print(t.shape)
print(sxx.shape)
plt.pcolormesh(t, f, sxx, cmap='gray')
plt.ylabel('Frequency[Hz]')
plt.xlabel('Time[s]')
cf = plt.gcf()
plt.show()
cf.savefig('/data2/process_data/caojihua/data/t.jpg')
#In[]:
import numpy as np
print(f.shape)
print(t.shape)
print(sxx.shape)

a = np.uint8((sxx - sxx.min()) / (sxx.max() - sxx.min()) * 255)
print(a.max())
plt.imshow(a)
plt.show()
np.count_nonzero(a)