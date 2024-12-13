DIRECTIONS = {
  "^": (-1, 0),
  ">": (0, 1),
  "v": (1, 0),
  "<": (0, -1)
}

NEXT_DIRECTION = {
  "^": ">",
  ">": "v",
  "v": "<",
  "<": "^"
}

def parse_file(filename):
  with open(filename, "r") as file:
    return [line.strip() for line in file]
  
def find_guard(grid):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] in DIRECTIONS.keys():
        direction = grid[y][x]
        return y, x, direction
  
def out_of_bounds(check_y, check_x, height, width):
  return check_y < 0 or check_y >= height or check_x < 0 or check_x >= width
  
def guard_traversal(y, x, direction):
  dy, dx = DIRECTIONS[direction]
  height = len(grid)
  width = len(grid[0])
  visited_locations = {(y, x)}
  out_of_area = False

  while not out_of_area:

    while True:
      new_y = y + dy
      new_x = x + dx
      if out_of_bounds(new_y, new_x, height, width):
        out_of_area = True
        break
      if grid[new_y][new_x] == "#":
        direction = NEXT_DIRECTION[direction]
        dy, dx = DIRECTIONS[direction]
        break
      y, x = new_y, new_x
      visited_locations.add((y, x))

    if out_of_area:
      break

  return len(visited_locations)
  
if __name__ == "__main__":
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "6.txt"
  grid = parse_file(filename)

  y, x, direction = find_guard(grid)
  guard_visit_count = guard_traversal(y, x, direction)

  print(guard_visit_count)

  