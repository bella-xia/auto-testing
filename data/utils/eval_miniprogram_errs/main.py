import json, os, csv
from check_first_50_miniprogram_data import WORKING_MINIAPP, COMPILATION_ERR_MINIAPP, OTHER_ERR_MINIAPP, PROBLEMS_DICT

def dump_to_csv(data, csv_file_path):
    """
    Dumps an array of dictionaries into a CSV file.
    
    Parameters:
    - data: list of dict, the data to write to the CSV file.
    - csv_file_path: str, the path to the CSV file.
    """
    if not data:
        print("Error: The data is empty.")
        return
    
    # Extract the field names (CSV headers) from the keys of the first dictionary
    fieldnames = data[0].keys()
    
    try:
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully written to {csv_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the CSV file: {e}")

def dump_to_json(data, json_file_path):
    """
    Dumps an array of dictionaries into a JSON file.
    
    Parameters:
    - data: list of dict, the data to write to the JSON file.
    - json_file_path: str, the path to the JSON file.
    """
    try:
        with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        print(f"Data successfully written to {json_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the JSON file: {e}")


if __name__ == '__main__':
    assert (len(WORKING_MINIAPP) + len(COMPILATION_ERR_MINIAPP) + len(OTHER_ERR_MINIAPP) == 50)
    total_data = []
    for work_instance in WORKING_MINIAPP:
        work_instance_dict = {'MiniApp': work_instance}
        work_instance_dict['Index'] = PROBLEMS_DICT.get("Passing", 0)
        work_instance_dict['Problem'] = ''
        work_instance_dict['Problem_Spec'] = ''
        total_data.append(work_instance_dict)
    for compile_err_instance in COMPILATION_ERR_MINIAPP:
        compile_err_instance['Index'] = PROBLEMS_DICT.get(compile_err_instance.get("Problem", "Other"), 6)
        if compile_err_instance.get('Problem_Spec', None) is None:
            compile_err_instance['Problem_Spec'] = ''
        total_data.append(compile_err_instance)
    for other_err_instance in OTHER_ERR_MINIAPP:
        other_err_instance['Index'] = PROBLEMS_DICT.get(other_err_instance.get("Problem", "Other"), 6)
        if other_err_instance.get('Problem_Spec', None) is None:
            other_err_instance['Problem_Spec'] = ''
        total_data.append(other_err_instance)
    ROOT_DIR = "/home/bella-xia/auto-testing/data/auxiliary_data"
    dump_to_csv(total_data, os.path.join(ROOT_DIR, 'miniprogram_data.csv'))
    dump_to_json(total_data, os.path.join(ROOT_DIR, 'miniprogram_data.json'))




