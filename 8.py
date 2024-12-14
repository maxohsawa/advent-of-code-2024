import itertools
import math

def parse_file(filename):
  with open(filename, "r") as file:
    return [[char for char in line.strip()] for line in file]
  
def create_freq_dictionary(grid):
  freq_to_coord = {}
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      
      freq = grid[y][x]
      if freq.isalnum():
        if freq not in freq_to_coord:
          freq_to_coord[freq] = []
        freq_to_coord[freq].append((y, x))

  return freq_to_coord
      
def calculate_antinodes(pair, grid, antinode_set, extend=False):
  coord1, coord2 = pair
  y1, x1 = coord1
  y2, x2 = coord2

  dy = y1 - y2
  dx = x1 - x2

  antinode1 = (y1 + dy, x1 + dx)
  antinode2 = (y2 - dy, x2 - dx)

  if is_within_bounds(antinode1, grid):
    antinode_set.add(antinode1)

  if is_within_bounds(antinode2, grid):
    antinode_set.add(antinode2)

  if extend:
    g = math.gcd(abs(dy), abs(dx))
    step_y = dy // g
    step_x = dx // g

    cy, cx = y2, x2
    while True:
      antinode_set.add((cy, cx))
      if (cy, cx) == (y1, x1):
        break
      cy += step_y
      cx += step_x

    ny, nx = y1 + step_y, x1 + step_x
    while is_within_bounds((ny, nx), grid):
      antinode_set.add((ny, nx))
      ny += step_y
      nx += step_x

    ny, nx = y2 - step_y, x2 - step_x
    while is_within_bounds((ny, nx), grid):
      antinode_set.add((ny, nx))
      ny -= step_y
      nx -= step_x

def is_within_bounds(antinode, grid):
  y, x = antinode
  return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def main():
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "8.txt"
  grid = parse_file(filename)
  freq_to_coord = create_freq_dictionary(grid)
  antinode_set = set()
  for key, coords in freq_to_coord.items():
    if len(coords) < 2:
      continue
    pairs = itertools.combinations(coords, 2)
    for pair in pairs:
      calculate_antinodes(pair, grid, antinode_set, extend=False)
  print("part 1:", len(antinode_set))

  antinode_set = set()
  for key, coords in freq_to_coord.items():
    antinode_set.update(coords)
    if len(coords) < 2:
      continue
    pairs = itertools.combinations(coords, 2)
    for pair in pairs:
      calculate_antinodes(pair, grid, antinode_set, extend=True)

  print("part 2:", len(antinode_set))

if __name__ == "__main__":
  main()