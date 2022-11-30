# Author: Haohan Zhu
# ID: 22308057
# Workplace: Trinity College Dublin
# Course: Computational Method (EEP55C22)
# Subject: Median filter applied to deal audio signal
# Project link: https://github.com/HaohanZhutcd/Computational_Method.git
# =============================================================================


from rw_audio import read_audio
from MeanSquareError import MSE
from Median_Execution import median_execution
from CubicSplinesFilter import CubicSplineInterpolation

corrupted_filename = './Audio_File/degraded.wav'
source_audio = './Audio_File/source_squabb.wav'


if __name__ == "__main__":
    # Execute medain filter
    median_execution(corrupted_filename, 3)
    # Execute Cubic Spline Interpolation
    filtered_data = CubicSplineInterpolation(corrupted_filename)
    # Calculate Mean Squared Error for Cubic Spline Interpolation
    data, Fs = read_audio(source_audio)
    mse = MSE(data, filtered_data)
    print("MSE for CubicSpline:", mse)
