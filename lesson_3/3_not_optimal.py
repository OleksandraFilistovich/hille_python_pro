from os import path

from pympler import asizeof


def word_finder(file_path, search_pattern, result_path) -> None:

    with open("source/results.txt", "w") as result_file:
        with open(file_path, "r") as f:
            for line in f.readlines():
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


search_line = input("Input line you want to search in 'rockyou':")
search_file = "./source/rockyou_encoded.txt"
result_file = "./source/results.txt"

word_finder(search_file, search_line, result_file)
print(line_n_size(result_file))
