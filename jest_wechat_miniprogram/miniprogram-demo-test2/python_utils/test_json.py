import json
import os

class PageQuery():
    def __init__(self, path_name):
        self.path_name = path_name
    
    def get_pages(self, project_name):
        full_path = os.path.join(self.path_name, project_name, 'app.json')
        with open(full_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data["pages"]