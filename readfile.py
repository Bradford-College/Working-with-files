import json

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            read_data = f.read()
            if not read_data:
                return []
            return json.loads(read_data)
    except (FileNotFoundError, json.JSONDecodeError):
        return []