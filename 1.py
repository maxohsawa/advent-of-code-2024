from collections import Counter

def parse_input(filename):
  with open(filename, "r") as file:
    lines = file.readlines()
  
  left_list = []
  right_list = []

  for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

  return left_list, right_list

def calculate_total_distance(left_list, right_list):
  left_list.sort()
  right_list.sort()
  sum = 0
  
  for left, right in zip(left_list, right_list):
    sum += abs(left - right)

  return sum

def calculate_similarity_score(left_list, right_list):
  right_freq = Counter(right_list)

  return sum(num * right_freq[num] for num in left_list if num in right_freq)

if __name__ == "__main__":
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "1.txt"

  left_list, right_list = parse_input(filename)

  total_distance = calculate_total_distance(left_list, right_list)

  print("part 1: total distance: ", total_distance)

  similarity_score = calculate_similarity_score(left_list, right_list)

  print("part 2: similarity score: ", similarity_score)