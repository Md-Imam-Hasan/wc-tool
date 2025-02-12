import argparse
import os
import sys


def count_chars(filename):
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            return sum(len(line) for line in file)
    except Exception as e:
        print(f'Error while opening file: {e}')


def count_bytes(filename):
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            file.seek(0, os.SEEK_END)
            return file.tell()
    except Exception as e:
        print(f'Error while opening file: {e}')


def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            return len(file.readlines())
    except Exception as e:
        print(f'Error while opening file: {e}')


def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            return sum(len(line.split()) for line in file)
    except Exception as e:
        print(f'Error while opening file: {e}')


def count_lines_from_stdin():
    return sum(1 for _ in sys.stdin)


def main():
    parser = argparse.ArgumentParser(
        description='Count the number of lines, words, and bytes in a file')

    parser.add_argument(
        'filename', default='-', nargs='?', type=str, help='Name of the file to count the number of lines, words, and bytes')

    parser.add_argument('-l', '--lines', action='store_true',
                        help='Count the number of lines in the file')

    parser.add_argument('-w', '--words', action='store_true',
                        help='Count the number of words in the file')

    parser.add_argument('-c', '--bytes', action='store_true',
                        help='Count the number of bytes in the file')

    parser.add_argument('-m', '--chars', action='store_true',
                        help='Count the number of characters in the file')

    args = parser.parse_args()

    if not args.lines and not args.words and not args.bytes and not args.chars:
        file_name = args.filename
        number_of_lines = count_lines(file_name)
        number_of_words = count_words(file_name)
        number_of_bytes = count_bytes(file_name)

        print(f'{number_of_lines} {number_of_words} {number_of_bytes} {file_name}')
    elif args.lines:
        file_name = args.filename
        if file_name == '-':
            number_of_lines = count_lines_from_stdin()
            print(number_of_lines)
        else:
            number_of_lines = count_lines(file_name)
            print(f'{number_of_lines} {file_name}')

    elif args.words:
        file_name = args.filename
        number_of_words = count_words(file_name)
        print(f'{number_of_words} {file_name}')
    elif args.bytes:
        file_name = args.filename
        number_of_bytes = count_bytes(file_name)
        print(f'{number_of_bytes} {file_name}')
    elif args.chars:
        file_name = args.filename
        number_of_chars = count_chars(file_name)
        print(f'{number_of_chars} {file_name}')


if __name__ == '__main__':
    main()
