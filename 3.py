def parse_file(filename):
  with open(filename, "r") as file:
    return file.read()
  
import re
muls_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
muls_and_do_dont_pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
muls_and_do_dont_compiled_pattern = re.compile(muls_and_do_dont_pattern)

def sum_of_muls_in_line(line):
  results = re.findall(muls_pattern, line)
  return sum(int(pair[0]) * int(pair[1]) for pair in results)

def conditional_sum_of_muls(line):

  muls = []
  state = True

  for match in muls_and_do_dont_compiled_pattern.finditer(line):
    token = match.group(0)
    if token == "do()":
      state = True
    elif token == "don't()":
      state = False
    elif state:
      x = match.group(2)
      y = match.group(3)
      muls.append((int(x), int(y)))

  return sum(mul[0] * mul[1] for mul in muls)
  
      
if __name__=="__main__":
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "3.txt"

  memory = parse_file(filename)

  part_1_sum = sum_of_muls_in_line(memory)

  print("part 1: ", part_1_sum)

  part_2_sum = conditional_sum_of_muls(memory)

  print("part 2: ", part_2_sum)