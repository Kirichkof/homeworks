from pathlib import Path
from random import randrange

current_dir = Path(__file__).parent
data_dir = current_dir / 'data_task_9.2'

with open(data_dir/ 'surnames.txt', mode ='rt', encoding ='utf-8') as file_read:
    with open(data_dir/ 'result.txt', mode ='wt', encoding='utf-8') as file_write:
        for line in file_read:
            surname = line.strip()
            choices = [str(randrange(1,99)) for _ in range(10)]
            str_choices = '#'.join(choices)
            file_write.write(f'{surname}#{str_choices}\n')