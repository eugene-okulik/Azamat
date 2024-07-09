class Flower:
    def __init__(self, color, fresh, stem_length, price, lifespan):
        self.color = color
        self.fresh = fresh
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, color, fresh, stem_length, price, lifespan):
        super().__init__(color, fresh, stem_length, price, lifespan)


class Lily(Flower):
    def __init__(self, color, fresh, stem_length, price, lifespan):
        super().__init__(color, fresh, stem_length, price, lifespan)


class Bouquet():
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flower = flower
        self.flowers.append(flower)
        self.total_lifespan = flower.lifespan + flower.fresh

    def calculate_wilting_time(self):
        return round(self.total_lifespan / len(self.flowers))

    def sort_flowers_by_parameter(self, parameter):
        return sorted(self.flowers, key=lambda x: getattr(x, parameter))

    def search_flowers_by_parameter(self, parameter, value):
        return [flower for flower in self.flowers if getattr(
            flower, parameter) == value]


# Создаем объекты цветов
rose1 = Rose("red", 5, 30, 150, 7)
rose2 = Rose("white", 4, 25, 120, 6)
lily1 = Lily("pink", 3, 38, 180, 5)

# Создаем букет и добавляем цветы
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(lily1)

# Расчет времени увядания букета
print(
    f"Среднее время увядания букета: {bouquet.calculate_wilting_time()} суток"
     )

# Сортировка цветов по параметру, передавая необходимый
sorted_flowers = bouquet.sort_flowers_by_parameter("price")
print("Цветы в букете отсортированы по цене:")
for flower in sorted_flowers:
    print(flower.price)

# Поиск цветов по параметру
searched_flowers = bouquet.search_flowers_by_parameter("color", "red")
print("Найденные цветы:")
for flower in searched_flowers:
    print(flower.color)
