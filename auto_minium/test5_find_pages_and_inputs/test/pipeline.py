import json
import os
import subprocess
import tracemalloc
from utils import write_to_file

def generate_config(input_data):
    config = {}
    for key, value in input_data.items():
        config[key] = value
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

def run_python_script(script_path):
    subprocess.run(['python', script_path, 'config.json'])


if __name__ == "__main__":
    tracemalloc.start()
    # project_path = "C:/Users/zhiha/OneDrive/Desktop/auto-testing/data"
    project_path = "C:/Users/zhiha/OneDrive/Desktop/miniapp_data/modified_miniapp"
    dev_tool_path = "C:/Program Files (x86)/Tencent/微信web开发者工具/cli.bat"
    script_path = 'C:/Users/zhiha/OneDrive/Desktop/auto-testing/auto_minium/test5_find_pages_and_inputs/test/main.py' 
    all_project_lists = os.listdir(project_path)
    for project in all_project_lists:
        input_data = {  
            "project_path": os.path.join(project_path, project),
            "dev_tool_path": dev_tool_path
            }
        write_to_file(str(project + "\n"), 'test_result_log.txt')
        generate_config(input_data)
        run_python_script(script_path)
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    write_to_file("\n Memory Allocation: \n", 'test_result_log.txt')
    write_to_file(top_stats[:10], 'test_result_log.txt')
