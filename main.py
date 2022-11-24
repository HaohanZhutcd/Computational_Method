# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

from detectionfile import detect_corrupted
from medianFilter_detection import medianFilter
from rw_audio import read_audio
# from rw_audio import write_audio
from rw_audio import comparison_degraded_restored_and_clean
# from MeanSquareError import MSE_Clean_and_Restored
from scipy.interpolate import CubicSpline
'''
corrupted_filename = './Audio_File/degraded.wav'
data, Fs = read_audio(corrupted_filename)
b_k = detect_corrupted(data, 0.8)
restoredfilename = './Audio_File/clean.wav'
filtered_data = medianFilter(corrupted_filename, b_k, 5, restoredfilename)
# filter_len = 5
# filtered_data = medianFilter(data, filter_len)

figure, axis = plt.subplots(2, 1)

plt.subplots_adjust(hspace=1)

axis[0].set_title('Waveform of the degraded audio')
axis[0].plot(data)
axis[0].set_xlabel('Sample Index')
axis[0].set_ylabel('Amplitude')

axis[1].set_title('Waveform of restoredq signal')
axis[1].plot(filtered_data)
axis[1].set_xlabel('Sample Index')
axis[1].set_ylabel('Amplitude')
plt.show()
if ord == 'q':
    plt.close()
filtered_data = np.array(filtered_data)

source_wav = './Audio_File/source_squabb.wav'
clean_data, _ = read_audio(source_wav)
# write_audio(newfilename, Fs, filtered_data)
comparison_degraded_restored_and_clean(corrupted_filename, restoredfilename)
# MSE_Clean_and_Restored(filtered_data, clean_data)
'''
corrupted_filename = './Audio_File/degraded.wav'
data, Fs = read_audio(corrupted_filename)
Fs_interval = 1 / Fs
end_time = len(data) * Fs_interval
x = np.arange(0, end_time, Fs_interval)
y = data
cs = CubicSpline(x, y)
xs = np.arange(-0.5, 9.6, 0.1)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'x', label='data')
ax.set_xlim(-0.5, 9.5)
ax.legend(loc='lower left', ncol=2)
plt.show()
