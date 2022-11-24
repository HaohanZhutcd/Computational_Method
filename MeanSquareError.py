# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

import numpy as np
# import math


def MSE_Clean_and_Restored(filtered_audio, clean_audio):
    sum_mse = 0
    for i in range(len(filtered_audio)):
        squared_error = np.double((np.double(filtered_audio[i]) -
                                   np.double(clean_audio[i])) ** 2)
        sum_mse = sum_mse + squared_error
    mse = ((sum_mse) / len(filtered_audio))
    # print("The mean squared error between restored and clean audio:", mse)
    return mse


# if __name__ == '__main__':
#     fied = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,3]
#     clen = [1,4,5,3,4,4,5,6,8,0,2,1,4,2,4,1]
#     MSE_Clean_and_Restored(fied, clen)
