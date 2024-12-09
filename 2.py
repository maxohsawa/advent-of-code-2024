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

def report_is_safe_with_dampener_bf(report):

  if report_is_safe(report):
    return True
  
  for i in range(len(report)):
    modified = report[:i] + report[i + 1:]
    if report_is_safe(modified):
      return True
  return False

def generate_sub_reports(report, i):
  if i - 1 >= 0:
    sub_report_1 = report[:i - 1] + report[i:]
  else:
    sub_report_1 = None

  sub_report_2 = report[:i] + report[i + 1:]

  if i + 1 < len(report):
    sub_report_3 = report[:i + 1] + report[i + 2:]
  else:
    sub_report_3 = None
  return sub_report_1, sub_report_2, sub_report_3

def report_is_safe_with_dampener(report):
  is_descending = report[0] > report[1]

  for i in range(len(report) - 1):
    a, b = report[i], report[i + 1]
    if (abs(a - b) not in range (1, 4)) or (is_descending and a < b) or (not is_descending and a > b):
      sub_report_1, sub_report_2, sub_report_3 = generate_sub_reports(report, i)
      sub_reports = generate_sub_reports(report, i)
      for sub_report in sub_reports:
        if sub_report is not None and report_is_safe(sub_report):
          return True
      return False
    
  return True

if __name__ == "__main__":
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "2.txt"

  reports = parse_file(filename)

  safe_reports_count = sum(1 for report in reports if report_is_safe(report))

  print("part 1: safe report count: ", safe_reports_count)

  safe_reports_with_dampener = sum(1 for report in reports if report_is_safe_with_dampener(report))

  print("part 2: safe with dampener count: ", safe_reports_with_dampener)

  # for report in reports:
  #   if report_is_safe_with_dampener(report) != report_is_safe_with_dampener_bf(report):
  #     print(report)

