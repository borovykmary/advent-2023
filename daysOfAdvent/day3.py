
class Day3:
    """
    --- Day 3: Advent calendar puzzles 5, 6 ---
    Methods:
        readTextFile() - read text file and replace words with numbers
        findPartNumbers() - find part numbers in each line
        getSumOfPartNumbers() - sum of part numbers
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def readTextFile(self):

        """
        Read text file and replace words with numbers
        Args:
            self.file_path(str): path to file
        Returns:
             list: list of lines
        """
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file.readlines()]
        return lines

    @staticmethod
    def horizontal_check(line, num_range):
        """
        Check if number is valid
        Args:
            line(str): line from text file
            num_range(list): range of numbers
        Returns:
            bool: True if number is valid, False if number is not valid
        """
        if num_range[0] > 0:
            if line[num_range[0] - 1] != '.':
                return True
        if num_range[1] < len(line):
            if line[num_range[1]] != '.':
                return True

        for char in line[num_range[0]:num_range[1]]:
            if (not char.isdigit()) and char != '.':
                return True

        return False

    @staticmethod
    def extract_adjacent_numbers(line, idx):
        """
        Extract adjacent numbers from the line
        Args:
            line(str): line from text file
            idx(int): index of the symbol
        Returns:
            list: list of adjacent numbers
        """
        adjacent_numbers = []
        left_pointer = idx - 1
        right_pointer = idx + 1

        if not line[idx].isdigit():
            current_number = ''
            while left_pointer >= 0 and line[left_pointer].isdigit():
                current_number = line[left_pointer] + current_number
                left_pointer -= 1
            if current_number:
                adjacent_numbers.append(int(current_number))

            current_number = ''
            while right_pointer < len(line) and line[right_pointer].isdigit():
                current_number += line[right_pointer]
                right_pointer += 1
            if current_number:
                adjacent_numbers.append(int(current_number))
        else:
            current_number = line[idx]
            while left_pointer >= 0 and line[left_pointer].isdigit():
                current_number = line[left_pointer] + current_number
                left_pointer -= 1
            while right_pointer < len(line) and line[right_pointer].isdigit():
                current_number += line[right_pointer]
                right_pointer += 1
            if current_number:
                adjacent_numbers.append(int(current_number))

        return adjacent_numbers

    def findPartNumbers(self):
        """
        Find part numbers in each line
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            list: list of part numbers
        """
        lines = self.readTextFile()
        part_numbers = []
        for idx_line, line in enumerate(lines):
            idx_num = 0
            while idx_num < len(line):
                num = line[idx_num]
                current_number = ''
                if num.isdigit():
                    pointer = idx_num + 1
                    current_number += num
                    while pointer < len(line) and line[pointer].isdigit():
                        current_number += line[pointer]
                        pointer += 1
                    if current_number:
                        num_range = [idx_num, idx_num + len(current_number)]
                        valid = []
                        left_right = self.horizontal_check(line, num_range)
                        valid.append(left_right)
                        if idx_line > 0:
                            check_up = self.horizontal_check(lines[idx_line - 1], num_range)
                            valid.append(check_up)
                        if idx_line < len(lines) - 1:
                            check_down = self.horizontal_check(lines[idx_line + 1], num_range)
                            valid.append(check_down)
                        if True in valid:
                            part_numbers.append(int(current_number))
                    idx_num += len(current_number)
                else:
                    idx_num += 1
        return part_numbers

    def findGearRatios(self):
        """
        Find gear ratios in the engine schematic
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            int: sum of gear ratios
        """
        lines = self.readTextFile()
        total_gear_ratios = 0

        for idx_line, line in enumerate(lines):
            for idx_symbol, symbol in enumerate(line):
                gear_numbers = []
                if symbol == '*':
                    gear_numbers += self.extract_adjacent_numbers(line, idx_symbol)
                    if idx_line > 0:
                        gear_numbers += self.extract_adjacent_numbers(lines[idx_line - 1], idx_symbol)
                    if idx_line < len(lines) - 1:
                        gear_numbers += self.extract_adjacent_numbers(lines[idx_line + 1], idx_symbol)

                if len(gear_numbers) == 2:
                    total_gear_ratios += (gear_numbers[0] * gear_numbers[1])

        return total_gear_ratios

    def getSumOfPartNumbers(self):
        """
        Sum of part numbers
        Args:
            self.findPartNumbers() - find part numbers in each line
        Returns:
            int: sum of part numbers
        """
        part_numbers = self.findPartNumbers()
        return sum(part_numbers)


print(Day3("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text3.txt").findPartNumbers())
print(Day3("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text3.txt").getSumOfPartNumbers())
print(Day3("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text3.txt").findGearRatios())

