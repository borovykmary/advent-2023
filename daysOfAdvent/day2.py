class Day2:
    """
    --- Day 2: Advent calendar puzzles 3, 4 ---
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def readTextFile(self):
        """
        Read text file and replace words with numbers
        Args:
            self.file_path(str): path to file
        Returns:
        list: list of dictionaries, each containing the game id and the game data
        """
        with open(self.file_path, "r") as file:
            lines = file.readlines()

        games = []
        for line in lines:
            game_id, game_data = line.split(':', 1)
            game_id = game_id.split()[1]
            games.append({'id': game_id, 'data': game_data.strip()})

        return games

    def fewestNumberOfCubes(self):
        """
        Find the fewest number of cubes that can be combined to make a cube with dimensions 12x13x14
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            int: the fewest number of cubes
        """
        games = self.readTextFile()
        powers = []
        for game in games:
            min_red = 0
            min_green = 0
            min_blue = 0
            sets = game['data'].split(';')
            for set in sets:
                parts = set.split(',')
                for part in parts:
                    part = part.strip()
                    cubes = int(part.split()[0])
                    color = part.split()[1]
                    if color == 'red':
                        min_red = max(min_red, cubes)
                    elif color == 'green':
                        min_green = max(min_green, cubes)
                    elif color == 'blue':
                        min_blue = max(min_blue, cubes)
            power = min_red * min_green * min_blue
            powers.append(power)
        return sum(powers)

    def possibleGamesIds(self):
        """
        Find possible games ids
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            list: list of possible games ids
        """
        games = self.readTextFile()
        possible_games_ids = []
        for game in games:
            max_red = 0
            max_green = 0
            max_blue = 0
            id = game['id']
            sets = game['data'].split(';')
            for set in sets:
                parts = set.split(',')
                for part in parts:
                    part = part.strip()
                    cubes = int(part.split()[0])
                    color = part.split()[1]
                    if color == 'red':
                        max_red = max(max_red, cubes)
                    elif color == 'green':
                        max_green = max(max_green, cubes)
                    elif color == 'blue':
                        max_blue = max(max_blue, cubes)
            if max_red <= 12 and max_green <= 13 and max_blue <= 14:
                possible_games_ids.append(id)
        return possible_games_ids

    def sumOfIds(self):
        """
        Sum of possible games ids
        Args:
            self.possibleGamesIds() - find possible games ids
        Returns:
            int: sum of possible games ids
        """
        possible_games_ids = self.possibleGamesIds()
        sum_of_ids = 0
        for id in possible_games_ids:
            sum_of_ids += int(id)
        return sum_of_ids


print(Day2("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text2.txt").fewestNumberOfCubes())
