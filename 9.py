def parse_file(filename):
  with open(filename, "r") as file:
    return file.read().strip()
  
def unpack_diskmap(diskmap):
  segments = []
  file_num = 0
  for i in range(0, len(diskmap), 2):
    mem_size = int(diskmap[i])
    for j in range(mem_size):
      segments.append(file_num)
    if i < len(diskmap) - 1:
      free_size = int(diskmap[i + 1])
      for j in range(free_size):
        segments.append(".")
    file_num += 1
  return segments

def print_data(data):
  print("".join([str(datum) for datum in data]))

def compress_data(data):
  left = 0
  right = len(data) - 1
  while left < right:
    while data[left] != ".":
      left += 1
    while data[right] == ".":
      right -= 1
    if left < right:
      data[left] = int(data[right])
      data[right] = "."
  return data

def check_sum(compressed_data):
  sum = 0
  for i, block in enumerate(compressed_data):
    if block != ".":
      sum += i * block
  return sum
  
def main():
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "9.txt"
  diskmap = parse_file(filename)
  data = unpack_diskmap(diskmap)
  compressed_data = compress_data(data)
  checksum = check_sum(compressed_data)
  print("part 1", checksum)

if __name__ == "__main__":
  main()