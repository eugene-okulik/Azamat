n = 23


def guess(number):
    while True:
        number = int(input())
        if number == n:
            print("Вы угадали число")
            break
        else:
            print("Попробуйте снова")
    return number


guess(21)
