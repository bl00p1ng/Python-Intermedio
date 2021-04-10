def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    print('*** CALCULAR DIVISORES **\n')

    num = input(':: Escribe un número: ')

    error_msg = """
    ⚠ Ingresaste una opción incorrecta
    Las únicas opciones validas son números mayores a 0
    NO puedes ingresar LETRAS o NÚMEROS NEGATIVOS
    """
    assert num.isnumeric() and int(num) > 0, error_msg

    print(divisors(int(num)))

    print('\nFin del Programa')


if __name__ == '__main__':
    run()
