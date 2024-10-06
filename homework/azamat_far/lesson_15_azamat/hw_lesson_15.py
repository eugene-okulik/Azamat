import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
                  )
cursor = db.cursor(dictionary=True)

query_1 = cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)"
                        )
cursor.execute(query_1, ('Azm', 'Farington'))
student_id = cursor.lastrowid

query_2 = cursor.execute("SELECT * from students where id = %s")
cursor.execute(query_2, (student_id))
print(cursor.fetchone())

query_3 = cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES \
        (%s, %s, %s)"
                        )
cursor.execute(query_3, ('13400_KTS', 'sep_2024', 'nov_2024'))
gr_id = cursor.lastrowid
query_4 = cursor.execute("SELECT * from `groups` where id = %s")
cursor.execute(query_4, (gr_id))
print(cursor.fetchone())

query_5 = cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s"
                        )
cursor.execute(query_5, (gr_id, student_id))
query_6 = cursor.execute("SELECT * from students where id = %s")
cursor.execute(query_6, (student_id))
print(cursor.fetchone())

query_7 = cursor.execute("INSERT INTO books (title) VALUES (%s)")
cursor.execute(query_7, ('Mechanics'))
book_id = cursor.lastrowid
query_8 = cursor.execute("SELECT * from books where id = %s")
cursor.execute(query_8, (book_id))
print(cursor.fetchone())

query_9 = cursor.execute(
    "UPDATE books SET taken_by_student_id = %s WHERE id = %s"
                        )
cursor.execute(query_9, (student_id, book_id))
query_10 = cursor.execute("SELECT * from books where id = %s")
cursor.execute(query_10, (book_id))
print(cursor.fetchone())

query_11 = cursor.execute("INSERT INTO subjets (title) VALUES (%s)")
cursor.execute(query_11, ('Прикладная математика'))

query_12 = cursor.execute("INSERT INTO subjets (title) VALUES (%s)")
cursor.execute(query_12, ('Информатика'))

query_13 = cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, \
        (SELECT id FROM subjets WHERE title = %s))"
                         )
cursor.execute(query_13, ('Математика', 'Прикладная математика'))

query_14 = cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, \
        (SELECT id FROM subjets WHERE title = %s))"
                         )
cursor.execute(query_14, ('Программирование', 'Информатика'))

query_15 = cursor.execute("INSERT INTO marks (value, lesson_id, student_id) \
    VALUES (%s, (SELECT id FROM lessons WHERE title = %s), \
        (SELECT id FROM students WHERE name = %s)), (%s, \
            (SELECT id FROM lessons WHERE title = %s), \
                (SELECT id FROM students WHERE name = %s))")
cursor.execute(
    query_15, ('5', 'Математика', 'Azm', '5', 'Программирование', 'Azm')
              )

query_16 = cursor.execute("SELECT * FROM marks WHERE student_id = %s")
cursor.execute(query_16, (student_id))

query_17 = cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s")
cursor.execute(query_17, (student_id))

query_18 = cursor.execute("SELECT b.title, g.title, m.value, l.title, su.title\
    FROM books AS b INNER JOIN students AS s ON b.taken_by_student_id = s.id \
        INNER JOIN `groups` AS g ON g.id = s.group_id \
            INNER JOIN marks AS m ON s.id = m.student_id \
                INNER JOIN lessons AS l ON m.lesson_id = l.id \
                    INNER JOIN subjets AS su ON l.subject_id = su.id \
                        WHERE name = %s")
cursor.execute(query_18, ('Azm'))

db.commit()

db.close()
