import os, re, json


def check_pattern(file_dir, re_pattern):
    with open(file_dir, "r", encoding="utf-8") as f:
        content = f.read()
        return re_pattern.search(content)


if __name__ == "__main__":
    ROOT = "C:/Users/zhiha/OneDrive/Documents/WeChat Files/Applet"
    all_dir_list = []
    target_miniapp = "wxece3a9a4c82f58c9"
    target_miniapp_dir = ROOT + "/" + target_miniapp
    folder_name = os.listdir(target_miniapp_dir)[0]
    target_miniapp_dir = target_miniapp_dir + "/" + folder_name + "/__APP__"

    plugin_keyword = re.compile(r"requirePlugin(")

    for root, dirs, files in os.walk(target_miniapp_dir):
        for file in files:
            if file.endswith(".js"):  # Only check .js files
                file_path = os.path.join(root, file)
                # print(f"surveyin file {file_path}")
                try:
                    plugin_flag = check_pattern(file_path, plugin_keyword)
                except Exception as e:
                    continue

                if plugin_flag is not None:
                    # print(plugin_flag, file_path)
                    all_dir_list.append(file_path)
        # break

    with open(f"{target_miniapp}_output.json", "w") as f:
        json.dump(all_dir_list, f, indent=4)
