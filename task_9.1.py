from pathlib import Path

current_dir = Path(__file__).parent
data_dir = current_dir / 'data_task_9.1'
with open(data_dir/ 'FIO.txt', mode ='rt', encoding ='utf-8') as file_read:
    with open(data_dir/ 'result.txt', mode ='wt', encoding='utf-8') as file_write:
        for line in file_read:
            surname, name, parent = line.strip().split(', ')
            file_write.write(f'{surname} {name[0]}. {parent[0]}. \n')