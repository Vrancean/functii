m = int(input('dati m: '))
n = int(input('dati n: '))
if m < n:
    def factorial(x):
        if x == 0:
            return 1
        return factorial(x-1) * x

    print(f'Numarul de combinari din {n} elemente cate {m} este {factorial(n)/factorial(m)/factorial(n-m)}')
else:
    print('m trebuie sa fie mai mic ca n')