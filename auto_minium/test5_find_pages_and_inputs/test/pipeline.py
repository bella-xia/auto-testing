import csv
import json
import os
import subprocess
from utils import write_to_file

def generate_config(input_data):
    config = {}
    for key, value in input_data.items():
        # Customize this based on your requirements
        config[key] = value
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

def run_python_script(script_path):
    subprocess.run(['python3', script_path, '/home/bella-xia/auto-testing/auto_minium/test5_find_pages_and_inputs/config.json'])

def main(inputs, script_path):
    for input_data in inputs:
        generate_config(input_data)
        run_python_script(script_path)

if __name__ == "__main__":
    project_path = "/home/bella-xia/auto-testing/data"
    dev_tool_path = "/home/bella-xia/wechat-web-devtools-linux/bin/wechat-devtools-cli"
    all_inputs = []
    all_project_lists = os.listdir(project_path)
    for project in all_project_lists:
        all_inputs.append({  
            "project_path": os.path.join(project_path, project),
            "dev_tool_path": dev_tool_path})
    write_to_file(str(project + "\n"), 'test_result_log.txt')
    script_path = '/home/bella-xia/auto-testing/auto_minium/test5_find_pages_and_inputs/test/main.py'  # Provide the path to your Python script
    main(all_inputs, script_path)
