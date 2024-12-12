def parse_file(filename):
  with open(filename, "r") as file:
    return file.readlines()
  
import re
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

def sum_of_muls_in_line(line):
  results = re.findall(pattern, line)
  return sum(int(pair[0]) * int(pair[1]) for pair in results)
  
if __name__=="__main__":
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "3.txt"

  memory = parse_file(filename)

  sum_of_multiplications = sum(sum_of_muls_in_line(line) for line in memory)

  print(sum_of_multiplications)