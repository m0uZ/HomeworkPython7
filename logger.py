from datetime import datetime

def log(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{};{}'.format(time, data))