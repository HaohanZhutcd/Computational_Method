# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

import numpy as np


def detect_corrupted(degraded_data, thresh):
    b_k = np.zeros((len(degraded_data),), dtype=int)
    for i in range(len(degraded_data)):
        if degraded_data[i] > thresh or degraded_data[i] < (-1 * thresh):
            b_k[i] = 1
        else:
            b_k[i] = 0
    return b_k
