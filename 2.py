def parse_file(filename):
  with open(filename, "r") as file:
    return [tuple(map(int, line.split())) for line in file]
  
def report_is_safe(report):
  if report[0] < report[1]:
    direction = 'inc'
  elif report[0] > report[1]:
    direction = 'dec'
  else:
    return False

  for i in range(len(report) - 1):
    a, b = report[i], report[i + 1]
    diff = b - a
    if abs(diff) not in (1, 2, 3):
      return False
    if direction == 'inc' and not (a < b):
      return False
    if direction == 'dec' and not (a > b):
      return False
  return True

def report_is_safe_with_dampener(report):

  if report_is_safe(report):
    return True
  
  for i in range(len(report)):
    modified = report[:i] + report[i + 1:]
    if report_is_safe(modified):
      return True
  return False

if __name__ == "__main__":
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "2.txt"

  reports = parse_file(filename)

  safe_reports_count = sum(1 for report in reports if report_is_safe(report))

  print("part 1: safe report count: ", safe_reports_count)

  safe_reports_with_dampener = sum(1 for report in reports if report_is_safe_with_dampener(report))

  print("part 2: safe with dampener count: ", safe_reports_with_dampener)

