import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = file.read()
    return json.loads(json_data)

def write_json_file(file_path, json_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)