from  pathlib import Path
from os import walk

current_path = Path(__file__).parent
data_path = current_path / 'some_data'

size_bounds = [100, 1000, 10000, 100000]
size_dict = {bound: 0 for bound in size_bounds}

for root, dirs, files in walk(data_path):
    for file in files:
        file_path = Path(root) / file
        file_size = file_path.stat().st_size
        for size in size_dict.keys():
            if file_size <= size:
                size_dict[size] += 1
                break

print(size_dict)