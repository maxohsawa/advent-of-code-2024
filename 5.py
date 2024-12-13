import math

ruleset = None

def parse_file(filename):
  with open(filename, "r") as file:
    lines = file.readlines()
    return lines
  
def parse_sections(lines):
  for i in range(len(lines)):
    if lines[i] == '\n':
      return {"rules": lines[:i], "updates": lines[i + 1:]}
    
def build_rule_set(rules):
  ruleset = {}
  for rule in rules:
    pair = rule.split("|")
    a = int(pair[0])
    b = int(pair[1])
    if a in ruleset:
      ruleset[a].add(b)
    else:
      ruleset[a] = {b}
  return ruleset

def parse_updates(updates):
  split_updates = [update.split(',') for update in updates]
  casted_updates = [[int(num) for num in update] for update in split_updates]
  return casted_updates

def check_compliance(update):
  position = {page: i for i, page in enumerate(update)}

  for A, Bs in ruleset.items():
    if A in position:
      for B in Bs:
        if B in position:
          if position[A] > position[B]:
            return False
  return True

def get_middle_value(lst):
  return lst[len(lst) // 2]

if __name__ == "__main__":
  import sys

  filename = sys.argv[1] if len(sys.argv) > 1 else "5.txt"

  lines = parse_file(filename)
  sections = parse_sections(lines)
  rules = sections["rules"]
  updates = parse_updates(sections["updates"])

  ruleset = build_rule_set(rules)
  
  check_compliance(updates[0])
  count = 0

  for update in updates:
    if check_compliance(update):
      count += get_middle_value(update)

  print(count)