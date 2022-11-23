# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================

import numpy as np


def MSE(filtered_audio, clean_audio):
    for i in range(len(filtered_audio)):
        squared_error = np.sqrt(filtered_audio[i] - clean_audio[i])
        mse = np.mean(np.sum(squared_error))
    return mse
