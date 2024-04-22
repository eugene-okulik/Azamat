import random
bonus = ['True', 'False']


def my_func(salary):
    dec = random.choice(bonus)
    if dec == 'True':
        return f"{salary},{dec} - '${salary + random.randint(0, 10000)}'"
    else:
        return f"{salary},{dec} - '${salary}'"


print(my_func(int(input())))
