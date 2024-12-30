def parse_file(filename):
  with open(filename, "r") as file:
    return file.read().strip()
  
# def unpack_diskmap(diskmap):
#   segments = []
#   file_num = 0
#   for i in range(0, len(diskmap), 2):
#     mem_size = int(diskmap[i])
#     for j in range(mem_size):
#       segments.append(file_num)
#     if i < len(diskmap) - 1:
#       free_size = int(diskmap[i + 1])
#       for j in range(free_size):
#         segments.append(".")
#     file_num += 1
#   return segments

# def print_data(data):
#   print("".join([str(datum) for datum in data]))

# def compress_data_part_1(data):
#   left = 0
#   right = len(data) - 1
#   while left < right:
#     while data[left] != ".":
#       left += 1
#     while data[right] == ".":
#       right -= 1
#     if left < right:
#       data[left] = int(data[right])
#       data[right] = "."
#   return data

# def check_sum(compressed_data):
#   sum = 0
#   for i, block in enumerate(compressed_data):
#     if block != ".":
#       sum += i * block
#   return sum

def convert_diskmap_to_block_representation(diskmap):
  blocks = []
  file_id = 0
  for i in range(len(diskmap)):
    # handle file block
    file_size = diskmap[i]
    blocks.append(("file", file_size, file_id))
    file_id += 1

    # handle free block
    if i < len(diskmap) - 1:
      i += 1
      free_size = diskmap[i]
      blocks.append(("free", free_size))
  
  return blocks

def main():
  import sys
  filename = sys.argv[1] if len(sys.argv) > 1 else "9.txt"
  diskmap = parse_file(filename)
  
  # data = unpack_diskmap(diskmap)
  # compressed_data_part_1 = compress_data_part_1(data)
  # checksum = check_sum(compressed_data_part_1)
  # print("part 1", checksum)

  # compressed_data_part_2 = compress_data_part_2(data)
  # checksum = check_sum(compressed_data_part_2)
  # print("part 2", checksum)

  block_representation = convert_diskmap_to_block_representation(diskmap)
  print(block_representation[:20])

if __name__ == "__main__":
  main()