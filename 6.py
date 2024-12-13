from collections import deque

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
    return [list(line.strip()) for line in file]
  
def find_guard(grid):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] in DIRECTIONS:
        direction = grid[y][x]
        return y, x, direction
  
def out_of_bounds(y, x, height, width):
  return y < 0 or y >= height or x < 0 or x >= width
  
def simulate_patrol(start_y, start_x, start_direction, grid, track_states=False):
  height = len(grid)
  width = len(grid[0])
  y, x = start_y, start_x
  direction = start_direction
  dy, dx = DIRECTIONS[direction]
  
  visited_positions = {(y, x)}
  visited_states = set()

  if track_states:
    visited_states.add((y, x, direction))

  while True:
    new_y = y + dy
    new_x = x + dx

    if out_of_bounds(new_y, new_x, height, width):
      return False if track_states else visited_positions
  
    if grid[new_y][new_x] == "#":
      direction = NEXT_DIRECTION[direction]
      dy, dx = DIRECTIONS[direction]
    else:
      y, x = new_y, new_x
      visited_positions.add((y, x))

      if track_states:
        state = (y, x, direction)
        if state in visited_states:
          return True
        visited_states.add(state)

def main():
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "6.txt"
  grid = parse_file(filename)

  start_y, start_x, start_direction = find_guard(grid)
  visited_cells = simulate_patrol(start_y, start_x, start_direction, grid, track_states=False)
  cell_visit_count = len(visited_cells)

  print("part 1: ", cell_visit_count)

  loop_count = 0
  original_char = '.'

  for (vy, vx) in visited_cells:
    if (vy, vx) == (start_y, start_x):
      continue
    old_char = grid[vy][vx]
    grid[vy][vx] = "#"
    if simulate_patrol(start_y, start_x, start_direction, grid, track_states=True):
      loop_count += 1

    grid[vy][vx] = old_char

  print("part 2: ", loop_count)

if __name__ == "__main__":
  main()