import os

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
                print(f"checking file {file_path}")
                if contains_word(file_path, word) is True:
                    container.append(file_path)
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            navigate_all_with_subscript(subscript, word, subdir_path, container)


if __name__ == '__main__':
    ROOT_DIR = '/home/bella-xia/auto-testing/data/5_vm2_groundtruth/wx7e3c3f665cd8e4e6'
    container = []
    navigate_all_with_subscript('js', 'VM2_INTERNAL_STATE_DO_NOT_USE_OR_PROGRAM_WILL_FAIL', ROOT_DIR, container)
    print(f"there are {len(container)} files that uses VM2 INTERNAL: ")
    for instance in container:
        print(instance)
