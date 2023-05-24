from  pathlib import Path

def remove_empty_dir(name: str) -> list:
    current_path = Path(__file__).parent
    data_path = current_path / name
    remove_names = []
    for item in data_path.iterdir():
        name = item.name
        try:
            item.rmdir()
        except OSError:
            continue
        remove_names.append(name)
    return remove_names

print(remove_empty_dir('data'))