import os, re, json, logging
from tqdm import tqdm

# from pipeline_utils.modify_wxml import format_wxml_style_attribute, find_wxml_files
# from pipeline_utils.modify_wxs import find_wxs_files
# from pipeline_utils.modify_babel import modify_babel_path
from pipeline_utils.modify_app_json import check_all_paths
from pipeline_utils.modify_config_json import modify_config_with_url
from pipeline_utils.modify_js import replace_plugin_instances


def pipeline_per_miniprogram(root_path, miniprogram_name):
    logger = logging.getLogger(miniprogram_name)
    logger.addHandler(logging.FileHandler(f"{miniprogram_name}_output.out"))
    f_data = f"\nSurveying miniprogram {miniprogram_name}\n"
    print(f_data)
    logger.info(f_data)
    # miniprogram_path = os.path.join(root_path, miniprogram_name)
    f_data = "\nStep 1: check config existence and modify config so that url can be processed unchecked\n"
    print(f_data)
    logger.info(f_data)
    modify_config_with_url(root_path, miniprogram_name, logger=logger)

    f_data = "Step 2: Eliminate all missing pages\n"
    print(f_data)
    logger.info(f_data)
    plugins_data = check_all_paths(root_path, miniprogram_name, logger=logger)

    f_data = "\nStep 3: Check all inclusion of plugins in js scripts\n"
    print(f_data)
    logger.info(f_data)
    all_plugin_script = {}
    if plugins_data is not None:
        for plugin_name, _ in plugins_data.items():
            match_pattern = re.compile(rf'requirePlugin("{plugin_name}")')
            match_instances = replace_plugin_instances(
                match_pattern, root_path, miniprogram_name, logger=logger
            )

            if len(match_instances) > 0:
                all_plugin_script[plugin_name] = match_instances

    with open(f"{miniprogram_name}_output.json", "w") as f:
        json.dump(all_plugin_script, f, indent=4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ROOT_PATH = (
        "C:/Users/zhiha/OneDrive/Desktop/auto-testing/miniapp_data/top50_data_copy"
    )

    miniprogram_list = ["wxb032bc789053daf4_腾讯健康"]
    # os.listdir(ROOT_PATH)
    for miniprogram_name in tqdm(miniprogram_list):
        pipeline_per_miniprogram(ROOT_PATH, miniprogram_name)
