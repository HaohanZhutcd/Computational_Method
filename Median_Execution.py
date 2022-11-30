# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================


"""
Execute the median filter
"""

# import time
import numpy as np
import matplotlib.pyplot as plt
from detectionfile import detect_corrupted
from medianFilter_detection import medianFilter
from rw_audio import read_audio
# from rw_audio import write_audio
from rw_audio import comparison_degraded_restored_and_clean
# from MeanSquareError import MSE_Clean_and_Restored
# from scipy.interpolate import CubicSpline
# from MeanSquareError import MSE


def median_execution(corrupted_filename, filter_length):
    data, Fs = read_audio(corrupted_filename)

    b_k = detect_corrupted(data, 0.5)

    restoredfilename = './Audio_File/clean.wav'

    filtered_data = medianFilter(corrupted_filename,
                                 b_k,
                                 filter_length,
                                 restoredfilename)

    figure, axis = plt.subplots(2, 1)

    plt.subplots_adjust(hspace=1)

    axis[0].set_title('Waveform of the degraded audio')
    axis[0].plot(data)
    axis[0].set_xlabel('Sample Index')
    axis[0].set_ylabel('Amplitude')

    axis[1].set_title('Waveform of restored signal')
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

    # Compare the mse between corrupted data and restored data
    # Ir is a function in the rw_audio.py
    mse = comparison_degraded_restored_and_clean(corrupted_filename,
                                                 restoredfilename)
    return data, filtered_data, b_k, mse


if __name__ == "__main__":
    corrupted_filename = './Audio_File/degraded.wav'
    filter_length = 3
    median_execution(corrupted_filename, filter_length)
    # filter_length = 3
    # mse_list = []
    # filter_list = []
    # corrupted_filename = './Audio_File/degraded.wav'
    # for i in range(20):
    #     filter_list.append(filter_length)
    #     _, _, _, mse = median_execution(corrupted_filename, filter_length)
    #     filter_length += 2
    #     mse_list.append(mse)
    # # filter_length
    # mse_list = np.array(mse_list)
    # print(mse_list)
    # print(filter_list)
    # plt.plot(filter_list, mse_list)
    # # giving a title to my graph
    # plt.title('mse')
    # # function to show the plot
    # plt.show()
