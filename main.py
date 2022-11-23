# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

from medianFilter import medianFilter
from rw_audio import read_audio, write_audio
from rw_audio import comparison_origin_and_clean

filename = './Audio_File/degraded.wav'
data, Fs = read_audio(filename)

filter_len = 5
filtered_data = medianFilter(data, filter_len)

figure, axis = plt.subplots(2, 1)

plt.subplots_adjust(hspace=1)

axis[0].set_title('Waveform of the degraded audio')
axis[0].plot(data)
axis[0].set_xlabel('Sample Index')
axis[0].set_ylabel('Amplitude')

axis[1].set_title('Waveform of clean signal')
axis[1].plot(filtered_data)
axis[1].set_xlabel('Sample Index')
axis[1].set_ylabel('Amplitude')
plt.show()

filtered_data = np.array(filtered_data)
newfilename = './Audio_File/clean.wav'
write_audio(newfilename, Fs, filtered_data)
comparison_origin_and_clean(filename, newfilename)
