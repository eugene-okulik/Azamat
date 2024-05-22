def dec_operation(func):
    def wrapper(first, second, operation):
        if first == second:
            return func(first, second, "+")
        elif first > second:
            return func(first, second, "-")
        elif second > first:
            return func(first, second, "/")
        elif first < 0 or second < 0:
            return func(first, second, "*")

    return wrapper


@dec_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first, second = (
    float(input("Введите первое число: ")), int(input("Введите \
        второе число: "))
)


calc(first, second, None)
print("Результат:", calc(first, second, None))
