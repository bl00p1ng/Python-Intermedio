def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    print('*** CALCULAR DIVISORES **\n')
    num = int(input(':: Escribe un número: '))
    print(divisors(num))
    print('\nFin del Programa')


if __name__ == '__main__':
    run()
