result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

# for result_1
num_res_1 = int(result_1[(result_1.index(":") + 2):])

# for result_2
num_res_2 = int(result_2[(result_2.index(":") + 2):])

# for result_3
num_res_3 = int(result_3[(result_3.index(":") + 2):])

print(num_res_1 + 10, num_res_2 + 10, num_res_3 + 10, sep='\n')
