def divisors(num):
    try:
        if num < 1:
            raise ValueError('⚠ Debes ingresar un número positivo')
        else:
            divisors = [i for i in range(1, num + 1) if num % i == 0]
            return divisors
    except ValueError as ve:
        print(ve)
        return f'{num} no es un valor válido'


def run():
    print('*** CALCULAR DIVISORES **\n')

    try:
        num = int(input(':: Escribe un número: '))
        print(divisors(num))
    except ValueError:
        print('⚠ Debes ingresar un número')

    print('\nFin del Programa')


if __name__ == '__main__':
    run()
