import itertools

def parse_file(filename):
  with open(filename, "r") as file:
    return [[char for char in line.strip()] for line in file]
  
def create_freq_dictionary(map):
  freq_to_coord = {}
  for y in range(len(map)):
    for x in range(len(map[0])):
      
      freq = map[y][x]
      if freq.isalnum():
        coord = (y, x)
        if freq in freq_to_coord:
          freq_to_coord[freq].append(coord)
        else:
          freq_to_coord[freq] = [coord]

  return freq_to_coord
      
def calculate_antinodes(pair):
  coord1, coord2 = pair
  y1, x1 = coord1
  y2, x2 = coord2

  dy = y1 - y2
  dx = x1 - x2

  antinode1 = (y1 + dy, x1 + dx)
  antinode2 = (y2 - dy, x2 - dx)

  # #1 (1, 3)
  # a1 (3, 4)
  # a2 (5, 5)
  # #2 (7, 6)
  # dy = y1 - y2 = -2
  # dx = x1 - x2 = -1

  return antinode1, antinode2

def is_within_bounds(antinode, map):
  y, x = antinode
  return 0 <= y < len(map) and 0 <= x < len(map[0])

def main():
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "8.txt"
  map = parse_file(filename)
  freq_to_coord = create_freq_dictionary(map)
  antinode_set = set()
  for key in freq_to_coord:
    if key in '.#':
      pass
    coords = freq_to_coord[key]
    pairs = itertools.combinations(coords, 2)
    for pair in pairs:
      antinode1, antinode2 = calculate_antinodes(pair)
      if is_within_bounds(antinode1, map):
        antinode_set.add(antinode1)
      if is_within_bounds(antinode2, map):
        antinode_set.add(antinode2)
  print(len(antinode_set))

if __name__ == "__main__":
  main()