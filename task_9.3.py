from pathlib import Path
from random import randrange

current_dir = Path(__file__).parent
data_dir = current_dir / 'data_task_9.2'

wins = [str(randrange(1,99)) for _ in range(3)]
with open(data_dir/ 'result.txt', mode ='rt', encoding ='utf-8') as file_read:
    for line in file_read:
        surname, *choices = line.strip().split('#')
        lenght = len(set(choices).intersection(wins))
        if lenght == 1:
            print(f'{surname} угадал одно число')