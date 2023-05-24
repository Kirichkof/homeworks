from  pathlib import Path

def create_project_dir(project_name: str) -> Path:
    if not project_name.isidentifier():
        raise TypeError
    current_path = Path(__file__).parent
    project_path = current_path / project_name
    if project_path.exists():
        raise ValueError
    project_path.mkdir()
    subdirs = ['backup', 'documents', 'music', 'others', 'pictures', 'videos']
    for subdir in subdirs:
        path = project_path / subdir
        path.mkdir()
    return project_path

test_name = ['prj1', 'prj 10']

for name in test_name:
    try:
        create_project_dir(name)
    except TypeError:
        print(f'Не валидное имя проекта: {name}')
    except ValueError:
        print(f'Такая директория уже есть: {name}')