class Day4:
    """
    --- Day 4 Advent calendar puzzles 5, 6 ---
    Methods:
        readTextFile() - read text file and replace words with numbers
        findWinningNumbers() - find winning numbers
        getTotalPoints() - get total points
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
            lines = file.readlines()
        return lines

    def findWinningNumbers(self):
        """
        Find winning numbers
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            dict: dictionary of identical numbers
        """
        identical_numbers = {}
        lines = self.readTextFile()
        for line in lines:
            card = line.replace(':', '|').split('|')
            card_number = card[0].strip()

            first_list_of_numbers = set(card[1].split())
            second_list_of_numbers = set(card[2].split())

            identical = first_list_of_numbers & second_list_of_numbers
            identical_numbers[card_number] = list(identical)
        return identical_numbers

    def getTotalPoints(self) -> int:
        """
        Get total points
        Args:
            self.findWinningNumbers() - find winning numbers
        Returns:
            int: total points
        """
        total_points = 0
        identical_numbers = self.findWinningNumbers()

        for card, numbers in identical_numbers.items():
            num_identical = len(numbers)
            if num_identical == 1:
                points = 1
            elif num_identical == 2:
                points = 2
            else:
                points = int(2 ** (num_identical - 1))

            total_points += points

        return total_points

    def getWonScratchcards(self):
        """
        Get won scratchcards
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            list: list of won scratchcards
        """
        cards = []
        lines = self.readTextFile()

        for line in lines:
            card = line.replace(':', '|').split('|')
            winning = set(card[1].split())
            mine = set(card[2].split())
            card = [1, winning, mine]
            cards.append(card)

        for c, card in enumerate(cards):
            count, winning, mine = card
            in_both = winning & mine
            matches = len(in_both)
            if matches == 0: continue

            for cc in range(c + 1, c + 1 + matches):
                cards[cc][0] += count
        return cards

    def getTotalScratchcards(self):
        """
        Get total scratchcards
        Args:
            self.getWonScratchcards() - get won scratchcards
        Returns:
            int: total scratchcards
        """
        cards = self.getWonScratchcards()
        total_scratchcards = 0
        for card in cards:
            total_scratchcards += card[0]
        return total_scratchcards


print(Day4("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text4.txt").getTotalPoints())
print(Day4("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text4.txt").getTotalScratchcards())
