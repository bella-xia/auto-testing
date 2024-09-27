import os, re


def check_pattern(file_dir, pattern):
    with open(file_dir, "r", encoding="utf-8") as f:
        content = f.read()
        return re.search(pattern, content)


def replace_plugin_instances(pattern, root_dir, target_miniapp, logger=None):
    f_data = f"checking for pattern {pattern}"
    print(f_data)
    if logger is not None:
        logger.info(f_data)
    all_dir_list = []
    target_miniapp_dir = os.path.join(root_dir, target_miniapp)
    for root, _, files in os.walk(target_miniapp_dir):
        for file in files:
            if file.endswith(".js"):  # Only check .js files
                file_path = os.path.join(root, file)
                # print(f"surveyin file {file_path}")
                try:
                    plugin_flag = check_pattern(file_path, pattern)
                except Exception as e:
                    continue

                if plugin_flag is not None:
                    f_data = f"finding plugin pattern {pattern} in {file_path}"
                    print(f_data)
                    if logger is not None:
                        logger.info(f_data)
                    # print(plugin_flag, file_path)
                    all_dir_list.extend(file_path)

    return all_dir_list
