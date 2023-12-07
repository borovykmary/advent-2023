class Day6:
    """
     --- Day 6 Advent calendar puzzles 9, 10 ---
    Methods:
        readTextFile() - read text file and replace words with numbers
        waysToBeatRecord() - find ways to beat record
        waysToBeatRecord2() - find ways to beat record with another parsing
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
        with open(self.file_path, 'r') as f:
            lines = f.readlines()

        time_line = lines[0].strip().split()
        distance_line = lines[1].strip().split()

        return time_line, distance_line

    def waysToBeatRecord(self):
        """
        Find ways to beat record
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            int: ways to beat record
        """
        time_line, distance_line = self.readTextFile()
        times = [int(t) for t in time_line[1:]]
        distances = [int(d) for d in distance_line[1:]]

        total_ways = 1
        for time, distance in zip(times, distances):
            ways_to_win = sum((time - t) * t > distance for t in range(time))
            total_ways *= ways_to_win

        return total_ways

    def waysToBeatRecord2(self):
        """
        Find ways to beat record
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            int: ways to beat record
        """
        time_line, distance_line = self.readTextFile()
        time = int(''.join(time_line[1:]))
        distance = int(''.join(distance_line[1:]))

        ways_to_win = sum((time - t) * t > distance for t in range(time))

        return ways_to_win


print(Day6("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text6.txt").waysToBeatRecord())
print(Day6("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text6.txt").waysToBeatRecord2())
