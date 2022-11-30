# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

"""
This file includes 3 funtions:
Read, write audio
Compare the result of corrupted and clean audio
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
# from numpy.fft import fft
from MeanSquareError import MSE
# import matplotlib
# from IPython.display import Audio
# from numpy.fft import ifft


# SciPy’s fast Fourier transform (FFT) implementation contains more features
# and is more likely to get bug fixes than NumPy’s implementation.

# check the version of matplotlib
# print(matplotlib.__version__)


def read_audio(filename):
    '''
    Read the audio file and display the spectrum

    Args:
        filename (str): auodio name

    Returns:
        data: an array included the audio signal
        Fs: sampling frequency of audio
    '''
    Fs, data = read(filename)

    # extract channel 0
    data = data[:, 0]
    # print("Sampling Frequency is:", Fs)
    data = data / 32767
    # samplingFrequency = Fs

    # ===============================================
    # Generally We dont need to use fft spectrum
    # Execute FFT(fast fourier transform)
    # Frequency domain representation
    # Normalize amplitude
    # ===============================================
    # fourierTransform = fft(data)/len(data)
    # Single sided spectrum
    # fourierTransform = 2*fourierTransform[range(int(len(data)/2))]
    # tpCount = len(data)
    # values = np.arange(int(tpCount/2))
    # timePeriod = tpCount/samplingFrequency
    # frequencies = values/timePeriod

    # Create subplot
    # figure, axis = plt.subplots(2, 1)
    # plt.subplots_adjust(hspace=1)

    # axis[0].set_title('Waveform of the audio')
    # axis[0].plot(data)
    # axis[0].set_xlabel('Sample Index')
    # axis[0].set_ylabel('Amplitude')

    # axis[1].set_title('Magnitude spectrum of corrupt signal')
    # axis[1].plot(frequencies, abs(fourierTransform))
    # axis[1].set_xlabel('Frequency')
    # axis[1].set_ylabel('Amp')
    # plt.show()

    # ===================================================
    # Frequency domain representation
    # This part is to display fft spectrum and waveform
    # Generally we don't use these codes
    # ===================================================
    # plt.figure(1)
    # plt.plot(frequencies, abs(fourierTransform))
    # plt.xlabel('Frequency')
    # plt.ylabel('Amplitude')
    # plt.title('Magnitude spectrum of speech')

    # plt.figure(2)
    # plt.plot(data)
    # plt.xlabel('Sample Index')
    # plt.ylabel('Amplitude')
    # plt.title('Waveform of the audio')
    # plt.show()

    if ord == 'q':
        plt.close()
    return data, Fs


def write_audio(output_filename, Fs_Output, data_Output):
    '''
    Write the audio file

    Args:
        output_filename: name of output audio
        Fs_Output: sampling frequency of output audio
        data_Output: output audio data
    '''

    data_Output = data_Output
    write(output_filename, Fs_Output, data_Output.astype(np.float32))


def comparison_degraded_restored_and_clean(filename, restored_filename):
    '''
    Compare the waveform of clean and corrupted
    '''
    Fs_ori, data_clean = read('./Audio_File/source_squabb.wav')
    data_clean = data_clean[:, 0]
    data_clean = data_clean / 32767

    Fs_degraded, data_degraded = read(filename)
    data_degraded = data_degraded[:, 0]
    data_degraded = data_degraded / 32767

    Fs_clean, data_restored = read(restored_filename)
    data_restored = data_restored

    mse = MSE(data_restored, data_clean)
    print("MSE between clean and restored: ", mse)

    # ======================================================
    # If you want to see the result of clean, degraded,
    # restored waveform, Please uncomment this part below.
    # But if you want to find the optimal filter length in
    # "Median_Execution.py", please comment it to short the
    # running time
    # ======================================================
    # figure, axis = plt.subplots(3, 1)
    # plt.subplots_adjust(hspace=1)

    # axis[0].set_title('Waveform of the degraded audio')
    # axis[0].plot(data_degraded)
    # axis[0].set_xlabel('Sample Index')
    # axis[0].set_ylabel('Amplitude')

    # axis[1].set_title('Waveform of restored signal')
    # axis[1].plot(data_restored)
    # axis[1].set_xlabel('Sample Index')
    # axis[1].set_ylabel('Amplitude')

    # axis[2].set_title('Waveform of clean signal')
    # axis[2].plot(data_clean)
    # axis[2].set_xlabel('Sample Index')
    # axis[2].set_ylabel('Amplitude')
    # plt.show()
    if ord == 'q':
        plt.close()
    return mse


if __name__ == '__main__':
    # filename = './Audio_File/source_squabb.wav'
    filename = './Audio_File/degraded.wav'
    read_audio(filename)
