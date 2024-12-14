import itertools

def parse_file(filename):
  with open(filename, "r") as file:
    return [line.strip() for line in file.readlines()]
  
def execute_operations(target, operands, operator_permutations):
  for permutation in operator_permutations:
    total = operands[0]
    for op, operand in zip(permutation, operands[1:]):
      if op == "+":
        total += operand
      else:
        total *= operand
    if total == target:
      return True
  return False
  
def verify_equation(equation):
  target_str, rest = equation.split(":")
  target = int(target_str)
  operands = [int(operand) for operand in rest.strip().split(" ")]
  operator_permutations = itertools.product('+*', repeat=len(operands) - 1)
  return target if execute_operations(target, operands, operator_permutations) else 0


def main():
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "7.txt"
  equations = parse_file(filename)
  total_targets = sum(verify_equation(equation) for equation in equations)
  print(total_targets)
  

if __name__ == "__main__":
  main()