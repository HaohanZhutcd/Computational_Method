import unittest
import numpy as np
# from detectionfile import detect_corrupted
from MeanSquareError import MSE
from medianFilter import medianFilter
from Median_Execution import median_execution


corrupted_filename = './Audio_File/degraded.wav'
nam = corrupted_filename
source_audio = './Audio_File/source_squabb.wav'
f_L = 3
corrupted_data, filtered_Signal, detection_bk, mse_fun = median_execution(nam,
                                                                          f_L)


class TestMedianFilter(unittest.TestCase):

    # test data length
    def test_IntegrityofData(self):
        data1 = len(corrupted_data)
        data2 = len(filtered_Signal)
        self.assertEqual(data1, data2)

    # test detecion array
    def test_detection(self):
        data1 = len(detection_bk)
        data2 = len(corrupted_data)
        self.assertEqual(data1, data2)

    # test mse
    def test_MSE(self):
        differences = np.subtract(corrupted_data, filtered_Signal)
        squared_differences = np.square(differences)
        sum_data = np.sum(squared_differences)

        result1 = MSE(corrupted_data, filtered_Signal)
        result2 = (sum_data) / (len(corrupted_data))

        self.assertEqual(result1, result2)

    # test filter length create correct window size in median
    def test_WindowSize(self):
        _, windowSize = medianFilter(corrupted_data, f_L)
        self.assertEqual(np.size(windowSize), f_L)


if __name__ == '__main__':
    unittest.main()
