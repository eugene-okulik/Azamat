import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv(override=True)  # Перезапись системных переменных override


db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor()

# Переменная для пути к файлу
base_path = os.path.dirname(__file__)
hw_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(hw_path, 'eugene_okulik', 'Lesson_16', 'data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
# Создание ключей и кортежа для проверки
for i in range(4):
    name = data[i]['name']
    sec_name = data[i]['second_name']
    gr_title = data[i]['group_title']
    b_title = data[i]['book_title']
    sub_title = data[i]['subject_title']
    les_title = data[i]['lesson_title']
    mr_value = data[i]['mark_value']
    # print(data)
    tup = (
        name, sec_name, gr_title, b_title, sub_title, les_title, mr_value
    )
    # Запрос в БД и проверка последующая наличия записи
    cursor.execute(f"""SELECT s.name, s.`second_name`, g.title,
    b.title, s2.title, l.title, m.value FROM
    `groups` g JOIN students s  ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjets s2 ON l.subject_id = s2.id
    WHERE s.name = '{name}' AND s.`second_name` = '{sec_name}'
    AND g.title = '{gr_title}' AND b.title = '{b_title}'
    AND s2.title = '{sub_title}' AND l.title = '{les_title}'
    AND m.value = '{mr_value}'""")
    names = cursor.fetchall()
    if tup in names:
        print(*names[0])
