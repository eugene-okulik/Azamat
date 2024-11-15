import argparse
import os

# Заводим аргументы для чтения логов
parser = argparse.ArgumentParser()
parser.add_argument("file", help="File name")
parser.add_argument("-n", "--name", help="name for search")
parser.add_argument("--full", help="type of result", action="store_true")
args = parser.parse_args()

# глобальные константы
DIRECTORY = os.listdir(args.file)
SEARCH_TEXT = args.name


def search(logs, search_name):
    for file in logs:
        full_path = os.path.join(args.file, file)
        with open(full_path, "r") as log_file:
            for i, line in enumerate(log_file.readlines()):
                if search_name in line:
                    print(f'Found in the line on index: {i} log file: {file}')
                    # Вывод части строки
                    first_index = line.find(search_name)
                    last_index = first_index + len(search_name)
                    end_line = line.index(line[-1])
                    space_count = 0
                    space_end_count = 0
                    start = 0
                    end = -1
                    # Вычисление 5 слов до искомого
                    for j in range(first_index, 0, -1):
                        if line[j - 1] == ' ' or line[j - 1] == ',':
                            space_count += 1
                        if space_count == 7:
                            start = j
                            break
                    # Вычисление 5 слов после искомого
                    for k in range(last_index, end_line):
                        if line[k + 1] == ' ' or line[k + 1] == ',':
                            space_end_count += 1
                        if space_end_count == 6:
                            end = k + 1
                            break
                    print(line[start:end])
                    break
            else:
                print("Nothing find")


search(DIRECTORY, SEARCH_TEXT)
