"""
Acceptance criteria:

    - user input describes the search word
    - all lines from the rockyou file which include the input are added to the new file called "results.txt"
    - information in the Console:
        - number of lines of a cerated file
        - total size of the created file (use Pympler 3-rd party library)
"""

from os import path

from pympler import asizeof


def file_reader(file_path):
    """Function creates generator which iterates over given file lines."""
    with open(file_path, "r") as f:
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                break


def word_finder(file_path, search_pattern, result_path) -> None:
    """Function finds given pattern line in lines of the given file.
    And writes them to the file."""
    with open(result_path, "w") as result_file:

        file_read = file_reader(file_path)

        for line in file_read:
            if search_pattern in line:
                result_file.writelines(line)


def line_n_size(file_path) -> tuple[int, int]:
    """Function returns size and amount of lines of the given file."""
    print(f"Size of file via os-module: {path.getsize(file_path)} B")
    file = open(file_path)
    file_content = file.read()
    file.close()

    count = file_content.count("\n")
    size = asizeof.asizeof(file_content)

    return f"Size of file via pympler-module: {size} B\nNumber of lines: {count}"


search_line = input("Input line you want to search in 'rockyou':").lower()
search_file = "./source/rockyou_encoded.txt"
result_file = "./source/results.txt"

word_finder(search_file, search_line, result_file)
print(line_n_size(result_file))
