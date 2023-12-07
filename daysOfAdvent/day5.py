class Day5:
    """
     --- Day 5 Advent calendar puzzles 7, 8 ---
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def readTextFile(self):
        map_lists = {
            'seed-to-soil': [],
            'soil-to-fertilizer': [],
            'fertilizer-to-water': [],
            'water-to-light': [],
            'light-to-temperature': [],
            'temperature-to-humidity': [],
            'humidity-to-location': [],
        }
        with open(self.file_path, 'r') as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                if line.startswith('seeds:'):
                    seeds = [int(x) for x in line.split()[1:]]
                    continue
                for map_name in map_lists:
                    if line.startswith(map_name):
                        map_list = map_lists[map_name]
                        break
                else:
                    temp = [int(x) for x in line.split()]
                    map_list.append((temp[1], temp[2], temp[0]))

            return seeds, list(map_lists.values())

    def get_destination(self, src, map_list):
        for s, r, d in map_list:
            if s <= src < s + r:
                return src - s + d
        return src

    def get_location(self, seed):
        temp = seed
        seeds, map_lists = self.readTextFile()
        for map_list in map_lists:
            temp = self.get_destination(temp, map_list)
        return temp

    def lowestLocationToInitial(self):
        seeds, _ = self.readTextFile()
        return min(self.get_location(seed) for seed in seeds)


print(Day5("/Users/marynaborovyk/Desktop/Advent_code/textFilesOfAdvent/input_text5.txt").lowestLocationToInitial())

