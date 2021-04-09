from raw_data.workers_data import DATA

def run():
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    all_Platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_Platzi_workers = list(map(lambda worker: worker["name"], all_Platzi_workers))

    old_people = [worker["name"] for worker in DATA if worker["age"] > 70]
    print(f'Old people: {old_people} \n')
    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]
    print(f'Adults: {adults} \n')

    for worker in all_Platzi_workers:
        print(worker)


if __name__ == '__main__':
    run()
