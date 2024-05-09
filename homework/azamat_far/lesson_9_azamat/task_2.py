temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
    22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]


def days(x):
    if x > 28:
        return True
    return False


hot_days = filter(days, temperatures)
new_days = list(hot_days)
print(new_days)
max_temprature = max(new_days)
min_temperture = min(new_days)
middle_temperature = sum(new_days) / len(new_days)
print(max_temprature, min_temperture, round(middle_temperature, 2), sep='\n')
