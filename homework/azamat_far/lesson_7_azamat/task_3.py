result_1 = "результат операции: 42"
result_2 = "результат операции: 54"
result_3 = "результат работы программы: 209"
result_4 = "результат: 2"
vol = (result_1, result_2, result_3, result_4)


def main_res(vol):
	for i in vol:
		position = i.split(": ")
		print(position[1])
		# Не могу победить, чтобы функция None не возвращала(


print(main_res(vol))
