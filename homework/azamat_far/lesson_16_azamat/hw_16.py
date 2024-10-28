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

# SQL запрос в БД
cursor.execute("""SELECT s.name, s.`second_name`, g.title, b.title, s2.title,
l.title, m.value FROM
`groups` g JOIN students s  ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.name = 'Ivan' or s.name = 'Petr' or s.name = 'Mark'""")
names = cursor.fetchall()

# Считывание строк таблицы
with open('F:\\py files\\study_AQA\\Azamat\\homework\\eugene_okulik\\Lesson_16\
\\data.csv', newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
# Создание кортежа со строкой из таблицы
for i in range(4):
    name = data[i]['name']
    sec_name = data[i]['second_name']
    gr_title = data[i]['group_title']
    b_title = data[i]['book_title']
    sub_title = data[i]['subject_title']
    les_title = data[i]['lesson_title']
    mr_value = data[i]['mark_value']
    tup = (
        name, sec_name, gr_title, b_title, sub_title, les_title, mr_value
        )
    # Проверка наличия в 'names' строки из файла
    for j in names:
        if tup in names:
            no_in_bd = i
# вывод строк, которых нет в БД
for k in range(4):
    if k != no_in_bd:
        print(data[k]['name'], data[k]['second_name'], end=' ')
        print(data[k]['group_title'], data[k]['book_title'], end=' ')
        print(data[k]['subject_title'], data[k]['lesson_title'], end=' ')
        print(data[k]['mark_value'])
