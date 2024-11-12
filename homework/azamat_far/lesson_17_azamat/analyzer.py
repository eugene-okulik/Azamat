import argparse
import os

# Заводим аргументы для чтения логов
parser = argparse.ArgumentParser()
parser.add_argument("file", help="File name")
parser.add_argument("-n", "--name", help="name for search")
parser.add_argument("--full", help="type of result", action="store_true")
args = parser.parse_args()

# Ввод полного пути до лога
log_path = input("Path to log: ")
# глобальные константы
DIRECTORY = os.listdir(log_path)
SEARCH_TEXT = args.name


def search(logs, search_name):
    for FILE in logs:
        full_path = os.path.join(log_path, FILE)
        with open(full_path, "r") as log_file:
            for i, line in enumerate(log_file.readlines()):
                if search_name in line:
                    print(f'The line: {line} on index: {i} log file: {FILE}')
                    # Вывод части строки
                    first_index = line.index(search_name)
                    last_index = first_index + len(search_name)
                    start = first_index - 5
                    end = last_index + 5
                    # Блок обработки возникновения ошибок поиска по индексу
                    if start < 0:
                        print(line[:end], end='\n')
                    elif end > len(line):
                        print(line[start:], end='\n')
                    else:
                        print(line[start:end], end='\n')
                    break
            else:
                print("Nothing find")


search(DIRECTORY, SEARCH_TEXT)
