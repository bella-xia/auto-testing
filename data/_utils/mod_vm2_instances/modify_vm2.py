import re, os

def contains_word(filepath, word):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            contents = file.read()
            return word in contents
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return False
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

def navigate_all_with_subscript(subscript, word, root_dir, container):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file.split('.')[-1] == subscript:
                # print(f"checking file {file_path}")
                if contains_word(file_path, word) is True:
                    container.append(file_path)
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            navigate_all_with_subscript(subscript, word, subdir_path, container)

def replace_internal_state(file_path):
    pattern = r'\{[^{}]*VM2_INTERNAL_STATE_DO_NOT_USE_OR_PROGRAM_WILL_FAIL[^{}]*\}'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()

        modified_contents = re.sub(pattern, '{}', contents)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_contents)

        print(f"Successfully replaced internal state instances in {file_path}")

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

if __name__ == '__main__':
    ROOT_DIR = '/home/bella-xia/auto-testing/data/5_vm2_groundtruth/wx881b6d478deb81b0_copy'
    container = []
    navigate_all_with_subscript('js', 'VM2_INTERNAL_STATE_DO_NOT_USE_OR_PROGRAM_WILL_FAIL', ROOT_DIR, container)
    print(f"there are a total of {len(container)} files to be modified")
    for file in container:
        replace_internal_state(file)

