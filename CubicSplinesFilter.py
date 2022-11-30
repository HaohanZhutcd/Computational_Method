# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

"""
Cubic Splines Interpolation
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.interpolate import CubicSpline
from detectionfile import detect_corrupted
from rw_audio import read_audio
from rw_audio import write_audio
from MeanSquareError import MSE


def CubicSplineInterpolation(corrupted_filename):
    '''
    Execute Cubic Spline Interpolation
    Calculate execution time

    Args:
        corrupted_filename (str): auodio name

    Returns:
        filtered_data: an array included the audio signal
    '''

    # start
    start_time = time.time()

    data, Fs = read_audio(corrupted_filename)

    # thresh = 0.5 becaues I added the magnitude
    # of clicks I added is from 0.5 ~ 0.6
    b_k = detect_corrupted(data, 0.5)

    plt.figure(1)
    plt.plot(data)
    plt.show()

    index_reject = []
    # Reject the parts are not clicks
    for i in range(len(data)):
        if b_k[i] == 1:
            index_reject.append(i)
        else:
            pass
    # print(index)

    filtered_data = data
    # index
    x_data = np.arange(len(filtered_data))
    # delete the index where is clicks
    # like (0,1,2,3,4) -> (0,1,2,4)
    # (3) is the index where has click so delete
    # the x and y of the clicks
    # reproduce a array of data
    y = np.delete(filtered_data, index_reject)
    x = np.delete(x_data, index_reject)

    cs = CubicSpline(x, y)
    # print(index_reject)

    # for i in range(len(index_reject)):
    for i in tqdm(range(len(index_reject))):
        filtered_data[index_reject[i]] = cs(index_reject)[i]

    output_Audio = './Audio_File/restored_with_CubicSplineInterpolation.wav'
    write_audio(output_Audio, Fs, filtered_data)

    end_time = time.time()
    execution_time = end_time - start_time
    print('CubicSplineInterpolation Execution time:', execution_time, 's')

    print("Done")

    plt.figure(2)
    plt.plot(filtered_data)
    plt.show()

    # figure, axis = plt.subplots(2, 1)
    # plt.subplots_adjust(hspace=1)

    # axis[0].set_title('Waveform of the degraded audio')
    # axis[0].plot(data)
    # axis[0].set_xlabel('Sample Index')
    # axis[0].set_ylabel('Amplitude')

    # axis[1].set_title('Waveform of restored signal')
    # axis[1].plot(filtered_data)
    # axis[1].set_xlabel('Sample Index')
    # axis[1].set_ylabel('Amplitude')
    # plt.show()

    # plt.figure(1)
    # plt.plot(filtered_data)
    # plt.show()

    # mse = MSE(filtered_data, clean_audio)
    return filtered_data


if __name__ == '__main__':
    corrupted_filename = './Audio_File/degraded.wav'
    filtered_data = CubicSplineInterpolation(corrupted_filename)
    source_audio = './Audio_File/source_squabb.wav'
    data, Fs = read_audio(source_audio)
    mse = MSE(data, filtered_data)
    print(mse)
