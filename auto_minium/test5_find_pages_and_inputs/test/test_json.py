import json
import os

class page_query():
    def __init__(self, project_name):
        self.JSON_PATH = os.path.join(
            "C:\\Users\\zhiha\\OneDrive\\Desktop\\auto-testing\\auto_minium\\data",
            project_name,
            "app.json")
        self.pages = []
        self.find_pages()
    
    def find_pages(self):
        with open(self.JSON_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.pages = data["pages"]
    
    def get_pages(self):
        return self.pages