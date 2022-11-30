# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

"""
Calculate mse between 2 data
"""

import numpy as np
# import math


def MSE(data1, data2):
    sum_mse = 0
    for i in range(len(data1)):
        squared_error = np.double((np.double(data1[i]) -
                                   np.double(data2[i])) ** 2)

        # print(squared_error)
        sum_mse = sum_mse + squared_error
        # print("sum_mse:", sum_mse)
    mse = ((sum_mse) / len(data1))
    # print("The mean squared error between restored and clean audio:", mse)
    return mse


if __name__ == '__main__':
    a = [0, 0, 0, 0, 0]
    b = [1, 2, 4, 3, -1]
    mse = MSE(a, b)
    print(mse)
