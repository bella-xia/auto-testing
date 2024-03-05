from flask import Flask, jsonify
import os
from test_json import PageQuery

app = Flask(__name__)

@app.route('/get_array')
def get_array():
    project_path = "C:/Users/zhiha/OneDrive/Desktop/auto-testing/data"
    all_project_lists = os.listdir(project_path)
    project_and_pages = []
    page_query = PageQuery(project_path)
    for project in all_project_lists:
        project_and_pages.append({
            'app_name' : project,
            'page_list': page_query.get_pages(project)
        })
    return jsonify(project_and_pages)

if __name__ == '__main__':
    app.run(debug=True)
