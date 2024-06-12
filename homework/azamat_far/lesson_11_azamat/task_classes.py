class Book():
    mat_pages = 'Бумага'
    text = True
    reserve = True
    if reserve:
        reserve = "зарезервирована"

    def __init__(self, name, author, pages_count):
        self.name = name
        self.author = author
        self.pages_count = pages_count


class SchoolBooks(Book):
    tasks = True
    if tasks:
        print("Домашнее задание")

    def __init__(self, name, author, pages_count, subject, school_class):
        super().__init__(name, author, pages_count)
        self.subject = subject
        self.school_class = school_class


book_1 = Book('Идиот', 'Достоевский', 500)
print(f"Название: {book_1.name}, Автор: {book_1.author}, страниц: \
{book_1.pages_count}, материал: {book_1.mat_pages}, {book_1.reserve}")

book_2 = Book('Преступление и наказание', 'Достоевский', 600)
print(f"Название: {book_2.name}, Автор: {book_2.author}, страниц: \
{book_2.pages_count}, материал: {book_2.mat_pages}")

book_3 = Book('Война и мир', 'Лев Толстой', 1000)
print(f"Название: {book_3.name}, Автор: {book_3.author}, страниц: \
{book_3.pages_count}, материал: {book_3.mat_pages}")

book_4 = Book('Отцы и дети', 'Тургенев', 400)
print(f"Название: {book_4.name}, Автор: {book_4.author}, страниц: \
{book_4.pages_count}, материал: {book_4.mat_pages}")

book_5 = Book('Мертвые души', 'Гоголь', 800)
print(f"Название: {book_5.name}, Автор: {book_5.author}, страниц: \
{book_5.pages_count}, материал: {book_5.mat_pages}")

school_book_1 = SchoolBooks('Алгебра', 'Иванов', 200, 'Математика', 9)
print(f"Название: {school_book_1.name}, Автор: {school_book_1.author}, \
страниц: {school_book_1.pages_count}, предмет: {school_book_1.subject}, \
класс: {school_book_1.school_class}, {school_book_1.reserve}")

school_book_2 = SchoolBooks('Механика', 'Перышкин', 250, 'Физика', 10)
print(f"Название: {school_book_2.name}, Автор: {school_book_2.author}, \
страниц: {school_book_2.pages_count}, предмет: {school_book_2.subject}, \
класс: {school_book_2.school_class}")

school_book_3 = SchoolBooks('Деловой русский', 'Константинова', 190, 'Русский язык', 11)
print(f"Название: {school_book_3.name}, Автор: {school_book_3.author}, \
страниц: {school_book_3.pages_count}, предмет: {school_book_3.subject}, \
класс: {school_book_3.school_class}")
