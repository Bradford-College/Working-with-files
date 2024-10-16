import json
from readfile import read_file

def write_file(file_path: str, data: dict):
    current_data = read_file(file_path)
    current_data.append(data)
    with open(file_path, 'w') as file:
        json.dump(current_data, file, indent=4)
    return 'Written Successfully'
