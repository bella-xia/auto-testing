import os, json


def read_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json_file(file_path, json_data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4)


def check_dirs(root_addr, root_dir, dir_list, logger=None):
    COMP_SET = {
        ".js",
        ".wxml",
        # ".json",  ".wxss" <-- these two might not be completely necessary?
    }
    exist_list = []
    missing_list = []

    for dir_name in dir_list:
        exist_bool = True
        for comp in COMP_SET:

            comp_dir = (
                os.path.join(root_addr, (dir_name + comp))
                if root_dir is None
                else os.path.join(root_addr, root_dir, (dir_name + comp))
            )
            normalized_path = os.path.normpath(comp_dir)
            if not os.path.exists(normalized_path):
                missing_list.append(dir_name)
                exist_bool = False
                break
        if exist_bool:
            exist_list.append(dir_name)
    return_val = {"exist": exist_list, "miss": missing_list}
    print(return_val)
    if logger is not None:
        logger.info(return_val)
    return return_val


def check_borderStyle(json_data):
    if json_data.get("tabBar") is not None:
        if json_data["tabBar"].get("borderStyle") is not None:
            color_str = json_data["tabBar"]["borderStyle"]
            if color_str != "black" and color_str != "white":
                return False
    return True


def check_all_paths(root_path, miniprogram_name, app_json_path=None, logger=None):
    MINIRPOGRAM_PATH = os.path.join(root_path, miniprogram_name)
    APP_JSON_PATH = (
        app_json_path if app_json_path else os.path.join(MINIRPOGRAM_PATH, "app.json")
    )

    json_data = read_json_file(APP_JSON_PATH)

    if json_data.get("subPackages", None) is not None:
        new_subPackages = []

        total_hit: int = 0
        total_miss: int = 0

        all_pages = check_dirs(MINIRPOGRAM_PATH, None, json_data["pages"])
        f_data = f"In total, there are {len(all_pages['exist'])} complete pages and {len(all_pages['miss'])} missing pages"
        print(f_data)
        if logger is not None:
            logger.info(f_data)
        pages_set = set(all_pages["exist"])

        for subpackage in json_data["subPackages"]:
            subpackage_data = check_dirs(
                os.path.join(
                    MINIRPOGRAM_PATH,
                ),
                subpackage["root"],
                subpackage["pages"],
                logger=logger,
            )

            existing_pages = []
            for subpackage_page in subpackage_data["exist"]:
                if subpackage["root"] + subpackage_page in pages_set:
                    pages_set.remove(subpackage["root"] + subpackage_page)
                    f_data = f"subPackage {subpackage['root']} page {subpackage_page} already in pages"
                    print(f_data)
                    if logger is not None:
                        logger.info(f_data)

                existing_pages.append(subpackage_page)

            if len(existing_pages) > 0:
                new_subPackages.append(
                    {"root": subpackage["root"], "pages": existing_pages}
                )
                total_hit += 1
            else:
                f_data = f"unable to find subPackage {subpackage['root']}. reducing from app.json"
                print(f_data)
                if logger is not None:
                    logger.info(f_data)
                total_miss += 1
        f_data = f"there are a total of {len(json_data['subPackages'])} subPackages, of which {total_miss} do not have corresponding files, and {total_hit} has"
        print(f_data)
        if logger is not None:
            logger.info(f_data)
        json_data["subPackages"] = new_subPackages
        json_data["pages"] = list(pages_set)

    plugins_data = None
    if json_data.get("plugins", None) is not None:
        with open(os.path.join(MINIRPOGRAM_PATH, "__plugins__.json"), "w") as f:
            json.dump(json_data["plugins"], f, indent=4)
        plugins_data = json_data["plugins"]
        del json_data["plugins"]

    # for now
    if json_data.get("preloadRule", None) is not None:
        del json_data["preloadRule"]

    write_json_file(APP_JSON_PATH, json_data)
    return plugins_data


if __name__ == "__main__":

    ROOT_PATH = "C:/Users/zhiha/OneDrive/Desktop/auto-testing/miniapp_data/top50_data"
    MINIRPOGRAM_NAME = "wx23d8d7ea22039466_班级小管家"

    MINIPROGRAM_DIR = os.path.join(ROOT_PATH, MINIRPOGRAM_NAME)
    check_all_paths(MINIPROGRAM_DIR)
