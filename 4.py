grid = None

def parse_file(filename):
  with open(filename, "r") as file:
    return [line.strip() for line in file]
  
DIRECTIONS = [
  (-1, 0), # north
  (-1, 1), # north-east
  (0, 1),  # east
  (1, 1),  # south-east
  (1, 0),  # south
  (1, -1), # south-west
  (0, -1), # west
  (-1, -1) # north-west
]

def check_direction(grid, y, x, dy, dx):
  height = len(grid)
  width = len(grid[0])

  if not (0 <= y + 3*dy < height and 0 <= x + 3*dx < width):
    return 0
  
  if grid[y + dy][x + dx] == 'M' and \
      grid[y + 2*dy][x + 2*dx] == 'A' and \
      grid[y + 3*dy][x + 3*dx] == 'S':
      return 1
  
  return 0
  
def count_xmasses(grid):

  height = len(grid)
  width = len(grid[0])
  count = 0


  for y in range(height):
    for x in range(width):
      if grid[y][x] == 'X':
        for (dy, dx) in DIRECTIONS:
          count += check_direction(grid, y, x, dy, dx)

  return count

if __name__ == "__main__":
  import sys

  filename = sys.argv[1] if len(sys.argv) > 1 else "4.txt"

  grid = parse_file(filename)

  sum_of_xmasses = count_xmasses(grid)

  print("part_1: ", sum_of_xmasses)