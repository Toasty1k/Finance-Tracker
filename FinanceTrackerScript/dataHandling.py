import json

def load_data(file_path='data.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"transactions": [], "budget": 0.0}

def save_data(data, file_path='data.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
