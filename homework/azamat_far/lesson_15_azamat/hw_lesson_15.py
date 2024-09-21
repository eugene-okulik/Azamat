import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)

cursor.execute(
    "INSERT INTO students (name, second_name) VALUES ('Azamat', 'Farrow')"
    )
student_id = cursor.lastrowid
cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchone())

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES \
        ('15100_KMPM', 'sep_2024', 'nov_2024')"
    )
gr_id = cursor.lastrowid
cursor.execute(f'SELECT * from `groups` where id = {gr_id}')
print(cursor.fetchone())

cursor.execute(
    f"UPDATE students SET group_id = {gr_id} WHERE id = {student_id}"
    )
cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO books (title) VALUES ('Ter_meh')")
book_id = cursor.lastrowid
cursor.execute(f'SELECT * from books where id = {book_id}')
print(cursor.fetchone())

cursor.execute(
    f"UPDATE books SET taken_by_student_id = {student_id} WHERE id = {book_id}"
    )
cursor.execute(f'SELECT * from books where id = {book_id}')
print(cursor.fetchone())
db.commit()

db.close()
