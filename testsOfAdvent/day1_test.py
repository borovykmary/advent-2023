import unittest

from daysOfAdvent.day1 import Day1


class TestDay1(unittest.TestCase):

    def test_readTextFile(self):
        day_1 = Day1("../textFilesOfAdvent/test_text1.txt")
        lines = day_1.readTextFile()
        self.assertEqual(lines, ['two1nine\n', 'eightwothree\n', 'abcone2threexyz\n',
                                 'xtwone3four\n', '4nineeightseven2\n', 'zoneight234\n', '7pqrstsixteen'])

    def test_findCalibrationValue(self):
        day_1 = Day1("../textFilesOfAdvent/test_text1.txt")
        day_1.calibration_values = [29, 83, 13, 24, 42, 14, 76]
        result = day_1.findCalibrationValue()
        self.assertEqual(result, [29, 83, 13, 24, 42, 14, 76])

    def test_sumOfCalibrationValues(self):
        day_1 = Day1("../textFilesOfAdvent/test_text1.txt")
        day_1.calibration_values = [29, 83, 13, 24, 42, 14, 76]
        result = day_1.sumOfCalibrationValues()
        self.assertEqual(result, 281)


if __name__ == "__main__":
    unittest.main()
