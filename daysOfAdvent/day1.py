import regex as re


class Day1:
    """
    --- Day 1: Advent Calendar puzzles 1, 2 ---

    Methods:
        readTextFile() - read text file and replace words with numbers
        findCalibrationValue() - find calibration value in each line
        sumOfCalibrationValues() - sum of calibration values

    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.calibration_values = self.findCalibrationValue()

    def readTextFile(self):
        """
        Read text file and replace words with numbers
        Args:
            self.file_path(str): path to file
        Returns:
             list: list of lines
        """
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        return lines

    def findCalibrationValue(self):
        """
        Find calibration value in each line
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            list: list of calibration values
        """
        lines = self.readTextFile()
        numbers = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
        ]
        numbers_string = '|'.join(numbers)
        calibration_values = []
        for line in lines:
            digits = re.findall(rf"(\d|{numbers_string})", line, overlapped=True)
            first = digits[0]
            last = digits[-1]
            if digits:
                if len(first) > 1:
                    first = numbers.index(first) + 1
                if len(last) > 1:
                    last = numbers.index(last) + 1
                linedigits = int(f"{first}{last}")
                calibration_values.append(linedigits)
        return calibration_values

    def sumOfCalibrationValues(self):
        """
        Sum of calibration values
        Args:
            self.findCalibrationValue() - find calibration value in each line
        Returns:
            int: sum of calibration values
        """
        calibration_values = self.findCalibrationValue()
        return sum(calibration_values)


print(Day1("../textFilesOfAdvent/input_text1.txt").sumOfCalibrationValues())