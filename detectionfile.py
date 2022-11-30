# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

"""
detect where have clicks
"""

import numpy as np


def detect_corrupted(degraded_data, thresh):
    '''
    if the index has click , b_k = 1
    '''
    b_k = np.zeros((len(degraded_data),), dtype=int)
    for i in range(len(degraded_data)):
        if degraded_data[i] >= thresh or degraded_data[i] <= (-1 * thresh):
            b_k[i] = 1
        else:
            b_k[i] = 0
    # print("bk:", b_k)
    return b_k
