import itertools

def parse_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def execute_operations_with_memo(target, operands):
    memo = {}

    def dfs(index, total):
        if (index, total) in memo:
            return memo[(index, total)]

        if index == len(operands):
            return total == target

        next_operand = operands[index]
        for operator in "+*|":
            if operator == "+":
                new_total = total + next_operand
            elif operator == "*":
                new_total = total * next_operand
            elif operator == "|":
                new_total = int(str(total) + str(next_operand))

            if dfs(index + 1, new_total):
                memo[(index, total)] = True  
                return True

        memo[(index, total)] = False
        return False

    return dfs(1, operands[0])

def verify_equation(equation):
    target_str, rest = equation.split(":")
    target = int(target_str)
    operands = [int(operand) for operand in rest.strip().split(" ")]
    return target if execute_operations_with_memo(target, operands) else 0

def main():
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else "7.txt"
    equations = parse_file(filename)
    total_targets = sum(verify_equation(equation) for equation in equations)
    print("part 2:", total_targets)

if __name__ == "__main__":
    main()