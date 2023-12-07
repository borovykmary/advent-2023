from collections import Counter


class Day7:
    """
     --- Day 7 Advent calendar puzzles 11, 12 ---
     Methods:
            readTextFile() - read text file and replace words with numbers
            getHandType() - get hand type
            rankOfCards() - rank of cards
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
        hands_bid = [(line.split()[0], int(line.split()[1])) for line in lines]
        return hands_bid

    def getHandType(self, hand):
        """
        Get hand type
        Args:
            hand(str): hand
        Returns:
            int: hand type
        """
        c = Counter(hand)
        counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
        counts[-1] += jokers
        match counts:
            case *_, 5:
                return 7
            case *_, 4:
                return 6
            case *_, 2, 3:
                return 5
            case *_, 3:
                return 4
            case *_, 2, 2:
                return 3
            case *_, 2:
                return 2
        return 1

    def getTotalWinning(self):
        """
        Get total winning
        Args:
            self.readTextFile() - read text file and replace words with numbers
        Returns:
            int: total winning
        """
        hands_bid = self.readTextFile()
        total_winning_1 = sum(
            rank * bid
            for rank, (*_, bid) in enumerate(
                sorted(
                    (self.getHandType(hand), *map("*23456789TJQKA".index, hand), bid)
                    for hand, bid in hands_bid
                ),
                1,
            )
        )
        hands_bid_part2 = [(hand.replace('J', '*'), bid) for hand, bid in hands_bid]
        total_winning_2 = sum(
            rank * bid
            for rank, (*_, bid) in enumerate(
                sorted(
                    (self.getHandType(hand), *map("*23456789TJQKA".index, hand), bid)
                    for hand, bid in hands_bid_part2
                ),
                1,
            )
        )
        return total_winning_1, total_winning_2


print(Day7("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text7.txt").getTotalWinning())
