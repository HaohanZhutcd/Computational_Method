# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================
"""
Median Filter not using numpy library
"""
import numpy as np
from rw_audio import read_audio
from rw_audio import write_audio


def medianFilter(degraded_name, detection_b_k, filter_len, outputfile):
    '''
    Take the original signal and the median filter window length.

    Args:
        signal_input (int): It is a 1-D array that is specific to corrupted
                            audio.
        detectionfile: b_k array
        filter_len (int): It is a value to identify the window length of
                          Median Filter

    Returns:
        filtered_Signal: An array of the same size as the input signal as the
                         output of the signal after the median filter has
                         been applied
    '''

    # Detect the median filter window length if odd or not
    if filter_len % 2 == 1:
        # Window length is a odd number and extract the half part of window
        # If the window length is 5, the extracted part is 2

        # The extracted part can be used to as
        # the part before or after the middle value
        pad_part = (filter_len - 1) // 2
        filtered_Signal = []
        signal_input, Fs = read_audio(degraded_name)

        for i in range(len(signal_input)):
            filter_window = []
            # In fact, the range of the for loop in python is started from 0
            # To follow my logic I want the array start from 1
            index_i = i + 1
            if index_i + pad_part < filter_len:
                # This conditional statemnt is to identify
                # the begining part of the signal

                # Take an example:
                # Signal: [1, 2, 3, 6, 10, 7, 2, 1] and Filter window is 5
                # Read the Index until [1, 2, 3, 6, 10] which the index = 3
                # (i = 2)
                # We only need to pad 0 before the window [1, 2, 3, 6, 10]

                # padding 0 before the signal data
                filter_window = [0] * (pad_part - index_i + 1)

                # This for loop is to append the data
                # from input data to filter window
                for j in range(int(filter_len - (pad_part - index_i + 1))):
                    filter_window.append(signal_input[j])

            elif ((index_i + pad_part) > len(signal_input)):
                # This conditional statemnt is to identify
                # the end part of the signal

                # Take an example:
                # Signal: [1, 2, 3, 6, 10, 7, 2, 1] and Filter window is 5
                # Read the Index after [6, 10, 7, 2, 1] which the index = 6
                # (i = 5)
                # We only need to pad 0 after the window [6, 10, 7, 2, 1]

                for k in range((i - pad_part), len(signal_input)):
                    # This for loop is to append the data
                    # from input data to filter window

                    filter_window.append(signal_input[k])

                for p in range(i + pad_part - (len(signal_input) - 1)):
                    # padding 0 after the signal data

                    filter_window.append(0)

            else:
                # The middle part work normally and not need to pad 0
                for z in range(filter_len):
                    filter_window.append(signal_input[i + z - pad_part])

            # Sort the value in the filter window
            filter_window.sort()

            # Create a new array to store the data filtered
            # filtered_Signal.append(filter_window[pad_part])
            if detection_b_k[i] == 0:
                filtered_Signal.append(signal_input[i])
            else:
                filtered_Signal.append(filter_window[pad_part])
            print("Progress: ",
                  '%.3f' % (np.double(index_i / len(signal_input)) * 100),
                  "%")
        # outputfile = './Audio_File/clean.wav'
        print("Done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        write_audio(outputfile, Fs, np.array(filtered_Signal))
        return filtered_Signal
    elif filter_len % 2 == 0:
        # if the window length is even
        print("Please replace the filter length in a odd number")
    else:
        # if the length is float or negative...
        print("Please check the filter length if it is integer number or not")
