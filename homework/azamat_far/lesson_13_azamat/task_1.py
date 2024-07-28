import os
import datetime


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')

hw_path = os.path.dirname(os.path.dirname(base_path))
evg_file_path = os.path.join(
    hw_path, 'eugene_okulik', 'hw_13', 'data.txt'
                            )
new_file_path = os.path.join(base_path, 'new_data.txt')


def read_file():
    with open(evg_file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        line_task = data_line[0]
        date_obj = data_line[3:29]
        new_date = datetime.datetime.strptime(date_obj, "%Y-%m-%d %H:%M:%S.%f")
        if line_task == '1':
            week_later = datetime.timedelta(days=7)
            result_line = new_date + week_later
            result_line = result_line.strftime("%Y-%m-%d %H:%M:%S.%f")
        elif line_task == '2':
            result_line = new_date.strftime('%A')
        else:
            now = datetime.datetime.now()
            result_line = str((now - new_date).days)
        new_file.write(f'{result_line}\n')
