import os
import sys


def count_chars(filename):
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        return sum(len(line) for line in file)
    
def count_bytes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file.seek(0, os.SEEK_END)
        return file.tell()
    
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return len(file.readlines()) 
    
def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(len(line.split()) for line in file)

def count_lines_from_stdin():
    return sum(1 for _ in sys.stdin)

command_line_option = sys.argv[1]
if command_line_option == '-c':
  file_name = sys.argv[2]
  number_of_bytes = count_bytes(file_name)
  print(number_of_bytes, file_name)
elif command_line_option == '-l':
  if len(sys.argv) > 2:
    file_name = sys.argv[2]
    number_of_lines = count_lines(file_name)
    print(number_of_lines, file_name)
  else:
    number_of_lines = count_lines_from_stdin()
    print(number_of_lines)
elif command_line_option == '-w':
  file_name = sys.argv[2]
  number_of_words = count_words(file_name)
  print(number_of_words, file_name)
elif command_line_option == '-m':
  file_name = sys.argv[2]
  number_of_char = count_chars(file_name)
  print(number_of_char, file_name)
elif len(command_line_option)>2:
  file_name = command_line_option
  number_of_lines = count_lines(file_name)
  number_of_words = count_words(file_name)
  number_of_bytes = count_bytes(file_name)
  print(number_of_lines, number_of_words, number_of_bytes, file_name)