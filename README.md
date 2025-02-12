# File Statistics Counter

This Python script is a command-line utility that counts various statistics in text files, similar to the Unix `wc` (word count) command. It can count lines, words, bytes, and characters in a given file or from standard input.

This is first challage from [Coding Challange](https://codingchallenges.fyi/) website: [Build Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc)


## Features

- Count lines, words, bytes, and characters in a file
- Read from a file or standard input


## Usage
python app.py [-h] [-l] [-w] [-c] [-m] [filename]

### Arguments

- `filename`: Name of the file to analyze. Use '-' for standard input. (Optional, defaults to '-')

### Options

- `-h`, `--help`: Show help message and exit
- `-l`, `--lines`: Count the number of lines in the file
- `-w`, `--words`: Count the number of words in the file
- `-c`, `--bytes`: Count the number of bytes in the file
- `-m`, `--chars`: Count the number of characters in the file

If no options are specified, the script will output the line, word, and byte counts.


## Examples

1. Count lines, words, and bytes in a file:
`python app.py test.txt`


2. Count only lines in a file:
`echo "Hello, world!" | python app.py -l`

4. Count characters in a file:
`python app.py -m test.txt`


## Requirements

- Python 3.x


## Error Handling

The script includes basic error handling for file operations. If there's an error while opening or reading a file, an error message will be displayed.