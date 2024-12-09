def parse_file(filename):
  with open(filename, "r") as file:
    return [tuple(map(int, line.split())) for line in file]
  
def report_is_safe(report):
  is_descending = report[0] > report[1]

  for a, b in zip(report, report[1:]):
    if abs(a - b) not in range (1, 4):
      return False
    if is_descending and a < b:
      return False
    if not is_descending and a > b:
      return False
    
    
    
  return True

if __name__ == "__main__":
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "2.txt"

  reports = parse_file(filename)

  safe_reports_count = sum(1 for report in reports if report_is_safe(report))

  print(safe_reports_count)