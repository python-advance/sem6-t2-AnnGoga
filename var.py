from itertools import count, islice


def fib_infinite_iterator(n):
    if n > 0:
        if n == 1:
            print('[0]')
        elif n > 1:
            res = [0, 1, ]
            for i in islice(count(2), n):
                res.append(res[i - 1] + res[i - 2])
            return res
    else:
        print('Число элементов должно быть целым и положительным!')


if __name__ == "__main__":
    n = int(input('Введите число элементов последовательности: '))
    print(f'fib_infinite_iterator({n}): \n', fib_infinite_iterator(n))
