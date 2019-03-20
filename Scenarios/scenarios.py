import requests
from threading import Thread

def scenario_one():
    for _ in range(10):
        r = requests.get('http://localhost:8080/algorithm', params={})
        print(r)

def scenario_two():
    files = {
        'file': ('weather.arff', open('weather.arff', 'rb')),
        'batchSize': (None, '10'),
        'useKernelEstimator': (None, '0'),
    }
    for _ in range(10):
        r = requests.post('http://localhost:8080/algorithm/NaiveBayes',files=files)
        print(r.json())

if __name__ == "__main__":
    user_input = ''
    while(user_input != 'e'):
        user_input = input('Which scenario would you like to run?')
        if user_input == '1':
            scenario_one()
        elif user_input == '2':
            scenario_two()
        elif user_input == '3':
            for i in range(10):
                worker = Thread(target=scenario_one)
                worker.setDaemon(True)
                worker.start()
                worker.join()
        elif user_input == '4':
            for i in range(100):
                worker = Thread(target=scenario_two)
                worker.setDaemon(True)
                worker.start()
                worker.join()
