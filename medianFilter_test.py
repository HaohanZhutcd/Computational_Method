import numpy as np
from medianFilter import medianFilter


def medianFilter_numpuFunction_verification(signal_input, filter_len):
    if filter_len % 2 == 1:
        pad_part = (filter_len - 1) // 2
        filtered_Signal_test = []
        # print("pad_part:", pad_part)
        for i in range(len(signal_input)):
            filter_window = []
            # print("i:", i)
            index_i = i + 1
            if index_i + pad_part < filter_len:
                # print(index_i + pad_part)
                filter_window = [0] * (pad_part - index_i + 1)
                # print(filter_window)
                # print("remind:", int(filter_len - (pad_part - index_i + 1)))
                for j in range(int(filter_len - (pad_part - index_i + 1))):
                    filter_window.append(signal_input[j])
                # print("filter_window:", filter_window)
            elif ((index_i + pad_part) > len(signal_input)):
                for k in range((i - pad_part), len(signal_input)):
                    # print("k:", k)
                    filter_window.append(signal_input[k])
                    # print("filter_window:", filter_window)
                for p in range(i + pad_part - (len(signal_input) - 1)):
                    # print("l:", l)
                    filter_window.append(0)
                # print("filter_window:", filter_window)
            else:
                for z in range(filter_len):
                    # print("z:", z)
                    filter_window.append(signal_input[i + z - pad_part])
            # print(np.median(filter_window))
            # print("filter_window:", filter_window)
            filtered_Signal_test.append(int(np.median(filter_window)))
        # print("filtered_Signal:", filtered_Signal)
        # print(len(filtered_Signal))
        return filtered_Signal_test
    elif filter_len % 2 == 0:
        print("Please replace the filter length in a odd number")
    else:
        print("Please check the filter length if it is integer number or not")


def compare_designed_and_given(my_design, numpy_result):
    if my_design == numpy_result:
        print("The result of median filter designed by me is equal to \
            the result of median funtion from numpy library")
        return True
    else:
        print("The result of median filter designed by me is not equal to \
        the result of median funtion from numpy library")
        return False


if __name__ == '__main__':
    signal = [1, 2, 3, 6, 10, 7, 2, 1]
    # print("The length of input data:", len(signal))
    filter_len = 3
    numpy_result = medianFilter_numpuFunction_verification(signal, filter_len)
    my_design = medianFilter(signal, filter_len)
    compare_designed_and_given(my_design, numpy_result)
