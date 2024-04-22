import sys
sys.set_int_max_str_digits(1000000)


def fibo_num(n):
    fib_prev, fib_current = 0, 1
    for i in range(1, n + 1):
        fib_next = fib_prev + fib_current
        fib_prev, fib_current = fib_current, fib_next
        if i == 5 or i == 200 or i == 1000 or i == 100000:
            yield fib_current


for i in fibo_num(100001):
    print(i, sep='\n')
