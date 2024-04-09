result_1 = "результат операции: 42"
result_2 = "результат операции: 54"
result_3 = "результат работы программы: 209"
result_4 = "результат: 2"
vol = (result_1, result_2, result_3, result_4)


def main_res(vol):
    for i in vol:
        print(int(i.split(": ")[1]) + 10)


main_res(vol)
