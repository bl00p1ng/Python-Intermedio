def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {"firstname": "Andrés", "lastname": "López"}

    super_list = [
        {"firstname": "Andrés", "lastname": "López"},
        {"firstname": "Tony", "lastname": "Stark"},
        {"firstname": "Peter", "lastname": "Parker"},
        {"firstname": "Hana", "lastname": "Uzaki"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')


if __name__ == '__main__':
    run()
